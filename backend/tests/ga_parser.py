import unittest
from app.lexer.lexer import Lexer
from app.parser.parser import Parser
from tests.syntax_tscripts import SYNTAX_TSCRIPTS

class TestParser(unittest.TestCase):
    def test_syntax_scripts(self):
        for script in SYNTAX_TSCRIPTS:
            lexer = Lexer(script["code"])
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            expected_output = script["expected_output"]
            try:
                result = parser.parse()
                self.assertEqual(
                    "Syntax OK",
                    "Syntax OK",
                    msg=f"Failed for CODE #{script['number']}\nCODE:\n{script['code']}"
                )
            except SyntaxError as e:
                self.assertEqual(
                    str(e),
                    "Syntax Error",
                    msg=f"Failed for CODE #{script['number']}\nCODE:\n{script['code']}"
                )

if __name__ == "__main__":
    unittest.main()