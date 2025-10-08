"""
Tools module
Contains helper utilities such as symbolic solvers or calculators.
"""

import math

class Tools:
    def calculate(self, expression: str):
        """
        Safely evaluate a math expression.
        """
        try:
            return eval(expression, {"__builtins__": {}, "math": math})
        except Exception as e:
            return f"Error: {e}"
