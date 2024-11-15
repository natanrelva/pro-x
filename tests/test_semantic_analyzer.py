
import unittest
from semantic_analyzer import SemanticAnalyzer

class TestSemanticAnalyzer(unittest.TestCase):
    def test_valid_workflow(self):
        parsed_data = {
            "StartAt": "State1",
            "States": {
                "State1": {"Type": "Task", "Next": "State2"},
                "State2": {"Type": "Choice", "Choices": [{"Next": "State3"}], "Default": "State4"},
                "State3": {"Type": "Task", "End": True},
                "State4": {"Type": "Fail"}
            }
        }
        analyzer = SemanticAnalyzer(parsed_data)
        analyzer.validate()  # Should not raise any exception

    def test_invalid_start_at(self):
        parsed_data = {
            "StartAt": "InvalidState",
            "States": {
                "State1": {"Type": "Task", "Next": "State2"}
            }
        }
        analyzer = SemanticAnalyzer(parsed_data)
        with self.assertRaises(ValueError):
            analyzer.validate()

if __name__ == "__main__":
    unittest.main()
    