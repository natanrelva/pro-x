
import unittest
from code_generator import CodeGenerator

class TestCodeGenerator(unittest.TestCase):
    def test_graph_data_generation(self):
        validated_data = {
            "StartAt": "State1",
            "States": {
                "State1": {"Type": "Task", "Next": "State2"},
                "State2": {"Type": "Choice", "Choices": [{"Next": "State3"}], "Default": "State4"},
                "State3": {"Type": "Task", "End": True},
                "State4": {"Type": "Fail"}
            }
        }
        generator = CodeGenerator(validated_data)
        graph_data = generator.generate_graph_data()
        self.assertIn("nodes", graph_data)
        self.assertIn("links", graph_data)
        self.assertEqual(len(graph_data["nodes"]), 4)
        self.assertEqual(len(graph_data["links"]), 3)

if __name__ == "__main__":
    unittest.main()
    