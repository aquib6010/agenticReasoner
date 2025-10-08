# src/agent/creative_ideator.py
from typing import List
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class CreativeIdeator:
    def __init__(self, model_name="microsoft/phi-2", device=None, temperature=0.9):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)
        self.temperature = temperature

    def brainstorm(self, prompt: str, n_ideas: int = 3) -> List[str]:
        """Generate creative or diverse reasoning paths using a smaller local LLM."""
        ideas = []
        for _ in range(n_ideas):
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
            outputs = self.model.generate(
                **inputs,
                max_length=200,
                temperature=self.temperature,
                do_sample=True,
                top_p=0.95
            )
            idea = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            ideas.append(idea.strip())
        return ideas
