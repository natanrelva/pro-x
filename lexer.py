
import json

class Lexer:
    def __init__(self, json_file):
        with open(json_file, "r") as file:
            self.workflow_data = json.load(file)

    def tokenize(self):
        """Tokenizes the JSON structure by ensuring it contains necessary keys."""
        if "StartAt" not in self.workflow_data or "States" not in self.workflow_data:
            raise ValueError("JSON do workflow precisa conter 'StartAt' e 'States'.")
        return self.workflow_data
    