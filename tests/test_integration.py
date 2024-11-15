
import unittest
from lexer import Lexer
from parser import Parser
from semantic_analyzer import SemanticAnalyzer
from code_generator import CodeGenerator

class TestIntegration(unittest.TestCase):
    def test_full_pipeline(self):
        # Lexical Analysis
        lexer = Lexer("data/step_function.json")
        tokens = lexer.tokenize()

        # Parsing
        parser = Parser(tokens)
        parsed_data = parser.parse()

        # Semantic Analysis
        analyzer = SemanticAnalyzer(parsed_data)
        analyzer.validate()

        # Code Generation
        generator = CodeGenerator(parsed_data)
        graph_data = generator.generate_graph_data()
        generator.generate_html(graph_data, "data/test_workflow_graph.html")

        self.assertIn("nodes", graph_data)
        self.assertIn("links", graph_data)
        self.assertGreater(len(graph_data["nodes"]), 0)
        self.assertGreater(len(graph_data["links"]), 0)

if __name__ == "__main__":
    unittest.main()
