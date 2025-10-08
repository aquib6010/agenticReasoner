"""
Trace Logger module
Logs step-by-step reasoning for transparency.
"""

import datetime

class TraceLogger:
    def __init__(self):
        self.traces = []

    def log(self, step, detail):
        timestamp = datetime.datetime.now().isoformat()
        self.traces.append({"time": timestamp, "step": step, "detail": detail})

    def get_trace(self):
        return self.traces
