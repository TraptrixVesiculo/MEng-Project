import os
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader,TextLoader
from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain_huggingface import HuggingFaceEmbeddings
from datasets import concatenate_datasets, load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer, TrainingArguments, pipeline, BitsAndBytesConfig
from langchain.chains import RetrievalQA
from concurrent.futures import ThreadPoolExecutor
from langchain_huggingface import HuggingFacePipeline
from datetime import date, time, datetime
import torch
import multiprocessing
from geval import GEval
import json
from onnx_eb import ONNXEmbedding 
#from ft import train_model
# from langchain_community.llms import LlamaCpp
# from llama_cpp import Llama
# pip install llama-cpp-python
# pip install sentence-transformers
# pip install accelerate pip install -U bitsandbytes

EMBEDDING_MODEL = "intfloat/e5-large-v2"
ONNX_PATH = "./onnx_models/e5_large/model.onnx"
MODEL_PATH = "E:/huggingface_models/Llama-3.1-8B-Instruct"
#MODEL_PATH = "E:/huggingface_models/Llama-3.1-8B/gguf/Llama-3.1-8B-F16.gguf"  # for gguf deployment
PERSIST_DIR = "./chroma_db"
KNOWLEDGE_DIR = "./RAG"
COURSENUM = "ECE9000"
FINE_TUNED_DIR = "E:/huggingface_models/Llama-3.1-8B-Instruct/lora_label_model"
sample_code = """
    def calculate_average(x):
        total = 0
        for i in x:
            total += i
        return total / len(x)
    """

class DualAgentSystem:
    def __init__(self):
        # Initialization
        self.device =  "cpu"

        # self.embedding_model = HuggingFaceEmbeddings(
        #     model_name=EMBEDDING_MODEL,
        #     model_kwargs={"device":self.device},
        #     encode_kwargs={"batch_size": 64,
        #                     "normalize_embeddings": True
        #     }
        # )
        # self.embedding_model = ONNXEmbedding(
        #     model_path="./onnx_models/e5_large/model.onnx", 
        #     model_name=EMBEDDING_MODEL
        # )

        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        else:
            try:
                import torch_directml
                dml_available = torch_directml.is_available()
            except ImportError:
                dml_available = False

            if dml_available:
                torch_directml.is_available()
                self.device = torch_directml.device()
            else:
                self.device = torch.device("cpu")
        print(f"Using device: {self.device}")

        # initialization
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16
        )

        lora_weights_exist = os.path.exists(FINE_TUNED_DIR) and os.path.exists(os.path.join(FINE_TUNED_DIR, "adapter_model.bin"))
        base_model = AutoModelForCausalLM.from_pretrained(
            MODEL_PATH,
            device_map="auto",
            quantization_config=quant_config,
            offload_state_dict=True
        )

        # Load the weight if exist
        if lora_weights_exist:
            print("Loading fine-tuned model weights...")
            try:
                from peft import PeftModel
                self.model = PeftModel.from_pretrained(
                    base_model,
                    FINE_TUNED_DIR
                )
                
            except Exception as e:
                print(f"Fail to load LoRA weights: {e}")
                print("Using basic model.")
                self.model = base_model
        else:
            print("Using basic model.")
            self.model = base_model
            
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=tokenizer,
            max_new_tokens=1500,
            torch_dtype=torch.float16,
            batch_size=1, 
            max_length=2500,
            do_sample=True,               # Random sampling
            temperature=0.4,              # creativity（0.1-1.0）
            top_p=0.9,                    
            repetition_penalty=1.2,       
            eos_token_id=tokenizer.eos_token_id,  
            pad_token_id=tokenizer.eos_token_id
        )

        self.llm = HuggingFacePipeline(
            pipeline=self.pipe)


        # Choose embedding model based on device type
        if torch.cuda.is_available():
            # Using Huggihgface embedding model (NVDIA)
            self.embedding_model = HuggingFaceEmbeddings(
                model_name=EMBEDDING_MODEL,
                model_kwargs={"device": "cuda"},
                encode_kwargs={
                    "batch_size": 64,
                    "normalize_embeddings": True
                }
            )
        else:
            # Using ONNX embedding model (AMD or CPU)
            self.embedding_model = ONNXEmbedding(
                model_path=ONNX_PATH, 
                model_name=EMBEDDING_MODEL
            )

        ## For llama-cpp deployment
        # self.llm = Llama(
        #     model_path=MODEL_PATH,
        #     model_kwargs={"use_cuda": True},
        #     n_gpu_layers=-1,  # offload the layers to GPU
        #     n_threads=8,      # CPU threads
        #     n_threads_batch=8,  
        #     main_gpu=0,       
        #     seed=1234,
        #     temperature=0.3,
        #     max_tokens=2048,
        #     n_ctx=4096,
        #     n_batch=512,
        #     f16_kv=True,
        #     verbose=True,
        #     offload_kqv=True, 
        #     tensor_split=[1.0]  
        # )

        self.vector_db = self._init_vector_db()
        self.feedback_agent = self._create_feedback_agent()
        self.debugging_agent = self._create_debugging_agent()
        self.data_collector = []

    def _init_vector_db(self):
        # Loading the doc
        loader = DirectoryLoader(
            KNOWLEDGE_DIR, 
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"}
        )
        docs = loader.load()
        
        # Add the number of meta
        for doc in docs:
            path_parts = doc.metadata['source'].split(os.sep)
            if len(path_parts) > 1:
                course_name = path_parts[-2]
                doc.metadata['course'] = course_name
                
                filename = path_parts[-1].lower()
                if 'assignment' in filename:
                    doc.metadata['doc_type'] = 'assignment'
                elif 'lecture' in filename:
                    doc.metadata['doc_type'] = 'lecture'
                else:
                    doc.metadata['doc_type'] = 'reference'
            
            doc.metadata['timestamp'] = datetime.now().isoformat()

        # Split the file
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )
        chunks = text_splitter.split_documents(docs)
        
        if os.path.exists(PERSIST_DIR):
            db = Chroma(
                persist_directory=PERSIST_DIR,
                embedding_function=self.embedding_model
            )
        else:
            db = Chroma.from_documents(
                documents=chunks,
                embedding=self.embedding_model,
                persist_directory=PERSIST_DIR,
                collection_metadata={"hnsw:space": "cosine"}
            )
            db.persist()
                
        
        return db
    
    def get_context_retriever(self, course_name=None):
        filters = {}
        if course_name:
            filters["course"] = course_name
        
        return self.vector_db.as_retriever(
            search_kwargs={
                "filter": filters,
                "k": 4  # return 4 related files
            }
        )
    
    def _create_feedback_agent(self):
        prompt = ChatPromptTemplate.from_template(
            """You are a senior software reviewer. 
            Your task is to evaluate the following code snippet and provide constructive feedback.

            --- CODE START ---
            {code}
            --- CODE END ---

            --- KNOWLEDGE CONTEXT ---
            {context}
            --- CONTEXT END ---

            You MUST give feedback in **all four** aspects below, even if there are no issues:  
            1. Naming clarity (Are variable, function, and class names descriptive and consistent?)  
            2. Robustness (Error handling, edge cases, defensive programming)  
            3. Readability (Formatting, comments, logical flow)  
            4. Style consistency (Follows style guides, consistent patterns)  

            **Rules:**  
            - When describing a problem, specify the **exact line number** or range.  
            - DO NOT provide complete rewritten code. You may give short code fragments only if necessary to illustrate a point.  
            - If there is no problem for an aspect, explicitly say "No major issues found."  
            - Final output MUST follow this format exactly:

            [Feedback]
            1. Naming clarity  
            - Problem: <description> (Location: Line X)  
            - Suggestion: <short suggestion>  

            2. Robustness  
            - Problem: <description> (Location: Line X)  
            - Suggestion: <short suggestion>  

            3. Readability  
            - Problem: <description> (Location: Line X)  
            - Suggestion: <short suggestion>  

            4. Style consistency  
            - Problem: <description> (Location: Line X)  
            - Suggestion: <short suggestion>  

            [Rating]
            Overall: <1-10 score>
            Explaination of overall rating: <briefly explain how you came up with your final score in 200 words>
            """
# """Write a short summary of Python programming."""
        )
        
        return (
            {"code": RunnablePassthrough(), "context": self.get_context_retriever(COURSENUM)}
            | prompt
            | self.llm
            | StrOutputParser()
        )
    
    def _create_debugging_agent(self):
        prompt = ChatPromptTemplate.from_template(
            """You are a senior debugging expert. Analyze the code and provide concise suggestions.

                Your Task is to list the potential errors in the following code and provide suggestions.

                --- CODE START ---
                {code}
                --- CODE END ---

                --- KNOWLEDGE CONTEXT ---
                {context}
                --- CONTEXT END ---

                **Rules:**  
                - When describing a problem, specify the **exact line number** or range.  
                - DO NOT provide complete rewritten code. You may give short code fragments only if necessary to illustrate a point.  
                - If there is no problem for an aspect, explicitly say "No major issues found."  
                - Final output for each potential error MUST follow this format exactly:

                • Error [X]: [Type]
                • Location: Line [N]
                • Suggestion: [Text]
                """ 
        )
        
        return (
            {"code": RunnablePassthrough(), "context": self.get_context_retriever(COURSENUM)}
            | prompt
            | self.llm
            | StrOutputParser()
        )
    
    def run_pipeline(self, code: str):
        print("~~~~~~~~~~~~~~~~~Running pipeline~~~~~~~~~~~~~~")
        feedback = self.feedback_agent.invoke(code)
        debug_prediction = self.debugging_agent.invoke(code)

        
        # with ThreadPoolExecutor(max_workers=2) as executor:
        #     feedback_future = executor.submit(self._run_feedback_agent, code)
        #     debug_future = executor.submit(self._run_debugging_agent, code)
            
        #     feedback = feedback_future.result()
        #     print("Feedback:", feedback)

        #     debug_prediction = debug_future.result()
        #     print("Debugging Suggestion:", debug_prediction)
        
        # Collect the data
        self._collect_data(code, feedback, debug_prediction)
        return {
            "feedback": feedback,
            "debug_prediction": debug_prediction
        }
        
    def _run_feedback_agent(self, code):
        cleaned_code = self._clean_text(code)
        return self.feedback_agent.invoke(code)
    
    def _run_debugging_agent(self, code):
        return self.debugging_agent.invoke(code)
    
    def _clean_text(self, text: str) -> str:
        text = text.encode('ascii', 'ignore').decode('ascii')
        text = text.replace('\x92', "'")
        text = text.replace('\x93', '"').replace('\x94', '"')
        
        return text
    
    # Collect output data
    def _collect_data(self, code: str, feedback: str, debug_prediction: str):
        self.data_collector.append({
            "code": code,
            "feedback": feedback,
            "debug_prediction": debug_prediction
            })
        
def run_dual_agent_system():
        # run in the individual process
        system = DualAgentSystem()
        result = system.run_pipeline(sample_code)
        print("=== FeedBack ===")
        print(result["feedback"])
        print("\n=== Debugging Suggestion ===")
        print(result["debug_prediction"])
        with open("result.json", "w") as f:
            json.dump(result, f)

def run_evaluation():
    with open("result.json", "r") as f:
        result = json.load(f)
    evaluator = GEval(model=MODEL_PATH)
    evaluation_result = evaluator.evaluate_feedback(
        code=sample_code,
        feedback=result["feedback"]
    )
    print(json.dumps(evaluation_result, indent=2))

# Run the program
if __name__ == "__main__":
    try:
        import torch_directml
        dml_available = torch_directml.is_available()
    except ImportError:
        dml_available = False
        
    system = DualAgentSystem()

    # run feedback generating
    agent_process = multiprocessing.Process(target=run_dual_agent_system)
    agent_process.start()
    agent_process.join()

    # run evaluation
    eval_process = multiprocessing.Process(target=run_evaluation)
    eval_process.start()
    eval_process.join()