import os
import json
import pandas as pd
from datasets import Dataset, load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
import torch

MODEL_PATH = "E:/huggingface_models/Llama-3.1-8B-Instruct"
DATA_PATHS = ["./fine-tune/FT_trainsets/01_Train.csv",
                "./fine-tune/FT_trainsets/03_Train.csv",
                "./fine-tune/FT_trainsets/08_Train.csv",
                "./fine-tune/FT_trainsets/Class_Train.csv",
                "./fine-tune/FT_trainsets/Method_Train.csv"
                ]
OUTPUT_DIR = "E:/huggingface_models/Llama-3.1-8B-Instruct/lora_label_model"
BATCH_SIZE = 2
EPOCHS = 3
LR = 1e-4
CUTOFF_LEN = 512

def detect_device():
    if torch.cuda.is_available():
        return torch.device("cuda"), "cuda"
    else:
        try:
            import torch_directml
            if torch_directml.is_available():
                return torch_directml.device(), "dml"
        except ImportError:
            pass
    return torch.device("cpu"), "cpu"

device, device_type = detect_device()
print(f"Using device: {device} ({device_type})")


def load_and_prepare_data(file_paths):
    dfs = []
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        
        # create the prompt by 3 different kinds of datasets

        # Experimental dataset: code smell
        if 'ComplexClass' in df.columns:
            if 'index' in df.columns:
                df = df.drop(columns=['index'])
            feature_cols = [col for col in df.columns if col != 'Non-smell']
            df['prompt'] = df[feature_cols].apply(
                lambda row: "Feature: " + "; ".join([f"{col}: {val}" for col, val in zip(feature_cols, row)]),
                axis=1
            )
            df['completion'] = df['Non-smell'].astype(str)
            
        # Quality dataset: class level
        elif 'Classlongname' in df.columns:
            feature_cols = [col for col in df.columns if col not in ['Classlongname', 'label']]
            df['prompt'] = df[feature_cols].apply(
                lambda row: "Feature: " + "; ".join([f"{col}: {val}" for col, val in zip(feature_cols, row)]),
                axis=1
            )
            df['completion'] = df['label'].astype(str)
            
        # Quality dataset: method level
        elif 'longname' in df.columns:
            feature_cols = [col for col in df.columns if col not in ['longname', 'label']]
            df['prompt'] = df[feature_cols].apply(
                lambda row: "Feature: " + "; ".join([f"{col}: {val}" for col, val in zip(feature_cols, row)]),
                axis=1
            )
            df['completion'] = df['label'].astype(str)
        
        dfs.append(df[['prompt', 'completion']])
    
    combined_df = pd.concat(dfs, ignore_index=True)
    return Dataset.from_pandas(combined_df)


dataset = load_and_prepare_data(DATA_PATHS)

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, use_fast=False)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token


def tokenize(example):
    text = f"{example['prompt']}\nLabel: "
    labels = example['completion']
    
    # expect label only
    full_text = text + labels
    tokenized = tokenizer(
        full_text,
        truncation=True,
        max_length=CUTOFF_LEN,
        padding="max_length",
        return_tensors="pt"
    )

    text_tokens = tokenizer(
        text,
        truncation=True,
        max_length=CUTOFF_LEN,
        padding="max_length",
        return_tensors="pt"
    )
    input_len = text_tokens["attention_mask"].sum().item()
    
    # Create a label mask, only calculate the loss of the label part
    labels_tensor = torch.full_like(tokenized["input_ids"], -100)
    labels_tensor[:, input_len:] = tokenized["input_ids"][:, input_len:]
    
    return {
        "input_ids": tokenized["input_ids"].squeeze(),
        "attention_mask": tokenized["attention_mask"].squeeze(),
        "labels": labels_tensor.squeeze()
    }

tokenized_dataset = dataset.map(tokenize, remove_columns=dataset.column_names)

quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16
        )
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    device_map="auto",
    quantization_config=quant_config,
    offload_state_dict=True,
    torch_dtype= torch.float16 if device_type != "cpu" else torch.float32
)
if device_type == "dml":
    model = model.to(device)

# LoRA config
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)

model = prepare_model_for_kbit_training(model)
model = get_peft_model(model, lora_config)

# training args
training_args = TrainingArguments(
    per_device_train_batch_size=BATCH_SIZE,
    gradient_accumulation_steps=4,
    warmup_steps=50,
    num_train_epochs=EPOCHS,
    learning_rate=LR,
    fp16=True,
    logging_steps=10,
    output_dir=OUTPUT_DIR,
    save_total_limit=2,
    save_strategy="epoch",
    optim="adamw_torch",
    remove_unused_columns=False,
)

trainer = Trainer(
    model=model,
    train_dataset=tokenized_dataset,
    args=training_args,
    tokenizer=tokenizer,
    data_collator=lambda data: {
        "input_ids": torch.stack([torch.tensor(d["input_ids"]) for d in data]),
        "attention_mask": torch.stack([torch.tensor(d["attention_mask"]) for d in data]),
        "labels": torch.stack([torch.tensor(d["labels"]) for d in data]),
    }
)


trainer.train()

model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print(f"LoRA model saved to {OUTPUT_DIR}")