
import unittest
from lexer import Lexer

class TestLexer(unittest.TestCase):
    def test_valid_json(self):
        lexer = Lexer("data/step_function.json")
        tokens = lexer.tokenize()
        self.assertIn("StartAt", tokens)
        self.assertIn("States", tokens)

    def test_invalid_json(self):
        with open("data/invalid_step_function.json", "w") as f:
            f.write('{ "States": {} }')  # Missing StartAt key
        lexer = Lexer("data/invalid_step_function.json")
        with self.assertRaises(ValueError):
            lexer.tokenize()

if __name__ == "__main__":
    unittest.main()
    