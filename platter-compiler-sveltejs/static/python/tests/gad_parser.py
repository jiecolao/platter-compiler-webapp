from typing import Any
import unittest
from app.lexer.lexer import Lexer
from app.parser.parser_program import Parser
from tests.syntax_tscripts import SYNTAX_TSCRIPTS

def check_parse(script: dict[str, Any]):
    lexer = Lexer(script["code"])
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    try:
        result = parser.parse()
        return "Syntax OK"
    except Exception as e:
        return str(e)

class TestParser(unittest.TestCase):
    def test_syntax_scripts(self):
        i = 0
        for script in SYNTAX_TSCRIPTS:
            expected_output = script["expected_output"]
            with self.subTest(case = i):
                self.assertEqual(check_parse(script),expected_output )
            i += 1

if __name__ == "__main__":
    unittest.main()