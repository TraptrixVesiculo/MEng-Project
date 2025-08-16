import json
import numpy as np
from tenacity import retry, stop_after_attempt, wait_exponential
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, BitsAndBytesConfig
from typing import Dict, Any, Optional
import re
import torch
from langchain_huggingface import HuggingFacePipeline
import requests

class GEval:
    def __init__(self, model: str = "E:/huggingface_models/Llama-3.1-8B-Instruct"):
        # Detect device
        self.device =  "cpu"
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

        # Model initialization
        tokenizer = AutoTokenizer.from_pretrained(model)
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16
        )
        model = AutoModelForCausalLM.from_pretrained(
            model,
            device_map="auto",
            quantization_config=quant_config,
            offload_state_dict=True
        )
        gen_pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=1500,
            torch_dtype=torch.float16,
            batch_size=1, 
            max_length=2500,
            do_sample=True,               # Random sampling
            temperature=0.3,              # creativity（0.1-1.0）
            top_p=0.9,                   
            repetition_penalty=1.2,       
            eos_token_id=tokenizer.eos_token_id,  
            pad_token_id=tokenizer.eos_token_id
        )

        self.pipe = HuggingFacePipeline(
            pipeline=gen_pipe)
        
    def evaluate_feedback(self, code: str, feedback: str) -> Dict[str, Any]:
        prompt = f"""
        You are a code feedback quality assessor, you will evaluate the quality of feedback based on the following three dimensions:

        1. Contextual Relevancy - Evaluate the relevance of the feedback to the code context.

        Criteria:
        a. Does the feedback accurately reflect the code content?
        b. Does it address specific issues?
        c. Does it omit important context?

        2. Answer Relevancy - Evaluate the relevance of the feedback suggestions.

        Criteria:
        a. Does it directly address the problem?
        b. Does it address the student's level?
        c. Does it avoid irrelevant details?

        3. Correctness - Evaluate the correctness of the technical suggestions.

        Criteria:
        a. Does it follow best practices?
        b. Does it address the core issue?
        c. Does it introduce new bugs?

        Grading criteria (1-5 points per dimension, accurate to one decimal place):
        5: Excellent - All criteria are fully met.
        4: Good - Most criteria are met, with some minor deficiencies.
        3: Fair - Most criteria are met, but not comprehensive.
        2: Poor - Partially meets the criteria with significant issues
        1: Poor - Barely meets the criteria

        ## Evaluation Materials:
        ### Original Code:
        {code}

        ### Feedback:
        {feedback}

        ## Output Requirements:
        Please output the evaluation results in JSON format, as follows:
        {{
            "contextual_relevancy": {{
                "score": <1-5>,
                "reason": "<reason for evaluation>"
            }},
            "answer_relevancy": {{
                "score": <1-5>,
                "reason": "<reason for evaluation>"
            }},
            "correctness": {{
                "score": <1-5>,
                "reason": "<reason for evaluation>"
            }}
        }}
        """
        
        try:
            # Invoke the pipeline
            response = self.pipe.pipeline(
                prompt,
                max_new_tokens=1000, 
                return_full_text=False,
                do_sample=True,
                temperature=0.2, 
                top_p=0.9
            )
            
            # Process the response
            if isinstance(response, list) and len(response) > 0:
                content = response[0].get('generated_text', '')
            elif isinstance(response, dict):
                content = response.get('generated_text', '')
            else:
                content = str(response)
            
            content = content.strip()
            print("="*50)
            print("Model response:")
            print(content)
            print("="*50)
            
                
        except Exception as e:
            import traceback
            traceback.print_exc()
            return {
                "contextual_relevancy": {"score": 0, "reason": f"Evaluation Failed: {str(e)}"},
                "answer_relevancy": {"score": 0, "reason": f"Evaluation Failed: {str(e)}"},
                "correctness": {"score": 0, "reason": f"Evaluation Failed: {str(e)}"}
            }