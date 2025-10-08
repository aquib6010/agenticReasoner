"""
Planner module
Decides how to approach a given logic problem and determines which subtasks are needed.
"""

# src/agent/planner.py
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class Planner:
    def __init__(self, model_name="microsoft/phi-2", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)

    def plan(self, problem: str) -> str:
        """Break the problem into smaller reasoning steps."""
        prompt = f"Decompose the following logical problem into clear reasoning steps:\n\n{problem}\n\nSteps:"
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        output = self.model.generate(**inputs, max_length=250)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

