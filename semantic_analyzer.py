
class SemanticAnalyzer:
    def __init__(self, parsed_data):
        self.workflow = parsed_data
        self.states = parsed_data["States"]

    def validate(self):
        """Performs semantic validation on the parsed data."""
        start_at = self.workflow["StartAt"]

        if start_at not in self.states:
            raise ValueError(f"Estado inicial '{start_at}' não está presente em 'States'.")

        for state_name, state_data in self.states.items():
            self._validate_state(state_name, state_data)
            
    def _validate_state(self, state_name, state_data):
        if state_data["Type"] in ["Succeed", "Fail"] and "Next" in state_data:
            raise ValueError(f"O estado '{state_name}' não deve ter 'Next'.")

        if state_data["Type"] == "Choice":
            if "Choices" not in state_data:
                raise ValueError(f"O estado de 'Choice' '{state_name}' não possui 'Choices'.")
            for choice in state_data["Choices"]:
                if choice["Next"] not in self.states:
                    raise ValueError(f"Transição inválida para o estado '{choice['Next']}'.")

        if "Default" in state_data and state_data["Default"] is not None:
            if state_data["Default"] not in self.states:
                raise ValueError(f"Transição 'Default' inválida para o estado '{state_data['Default']}'.")
