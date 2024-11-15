
import unittest
from lexer import Lexer
from parser import Parser

class TestParser(unittest.TestCase):
    def test_valid_structure(self):
        lexer = Lexer("data/step_function.json")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        parsed_data = parser.parse()
        self.assertIn("StartAt", parsed_data)
        self.assertIn("States", parsed_data)

    def test_empty_states(self):
        tokens = {"StartAt": "State1", "States": {}}
        parser = Parser(tokens)
        parsed_data = parser.parse()
        self.assertEqual(parsed_data["States"], {})

if __name__ == "__main__":
    unittest.main()
    