from transformers import AutoTokenizer
import onnxruntime as ort
import numpy as np

class ONNXEmbedding:
    def __init__(self, model_path="onnx/model.onnx", model_name="BAAI/bge-small-en-v1.5"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.session = ort.InferenceSession(model_path, providers=["DmlExecutionProvider", "CPUExecutionProvider"])

    def embed_documents(self, texts):
        return [self._embed(t) for t in texts]

    def embed_query(self, text):
        return self._embed(text)

    def _embed(self, text):
        # Tokenize
        inputs = self.tokenizer(text, return_tensors="np", padding=True, truncation=True)
        valid_keys = {inp.name for inp in self.session.get_inputs()}
        ort_inputs = {k: v.astype(np.int64) for k, v in inputs.items() if k in valid_keys}

        # Run ONNX
        outputs = self.session.run(None, ort_inputs)
        embedding = outputs[1]
        return embedding[0].tolist()