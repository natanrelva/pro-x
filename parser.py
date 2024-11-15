class Parser:
    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        """Parse the tokens into a format ready for semantic analysis."""
        states = self.tokens["States"]
        parsed_structure = {"StartAt": self.tokens["StartAt"], "States": {}}

        for state_name, state_data in states.items():
            parsed_state = {
                key: value
                for key, value in state_data.items()
                if value is not None  # Remove keys with None values
            }
            parsed_structure["States"][state_name] = parsed_state

        return parsed_structure
