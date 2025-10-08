"""
Verifier module
Checks correctness and consistency of answers.
"""

# src/agent/verifier.py
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class Verifier:
    def __init__(self, model_name="microsoft/phi-2", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)

    def verify(self, problem: str, execution_result: str) -> str:
        """Cross-check reasoning and produce final verified answer."""
        prompt = (
            f"Problem: {problem}\n"
            f"Proposed reasoning: {execution_result}\n\n"
            f"Check the logic carefully and provide the final verified answer:"
        )
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        output = self.model.generate(**inputs, max_length=200)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
