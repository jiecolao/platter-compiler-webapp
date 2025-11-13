import unittest
import os
from pprint import pformat
from app.lexer.lexer import Lexer
from app.lexer.token import Token

SAMPLES_DIR = "./tests/lexer_programs/"

class TestPlatterLexerStrings(unittest.TestCase):

    def test_all_files(self):
        self.maxDiff = None
        platter_files = [f for f in os.listdir(SAMPLES_DIR) if f.endswith(".platter")]
        for pf in platter_files:
            with self.subTest(platter_file=pf):
                filepath = os.path.join(SAMPLES_DIR, pf)
                with open(filepath, "r", encoding="utf-8") as f:
                    source = f.read()
                lexer = Lexer(source)
                tokens = "\n".join(t.type for t in lexer.tokenize())

                output_file = pf.replace(".platter", ".output")
                output_path = os.path.join(SAMPLES_DIR, output_file)
                if not os.path.exists(output_path):
                    self.fail(f"Missing output file for {pf}")

                with open(output_path, "r", encoding="utf-8") as f:
                    expected = f.read().strip()

                self.assertEqual(tokens, expected)

    string_tests = [
        {
            "code": 'piece;',
            "expected_types": [Token.InvalidIdentifier, "Invalid Character"],
        },
        {
            "code": 'piece of x = 5;',
            "expected_types": ["piece", "of", "id", "=", "piece_lit", ";"],
        },
        {
            "code": 'piece&',
            "expected_types": [Token.InvalidIdentifier, "Invalid Character"],
        },
        {
            "code": 'piece_',
            "expected_types": ["id"],
        },
        {
            "code": '12',
            "expected_types": ["piece_lit"],
        },
        {
            "code": 'copy = piece_lit;',
            "expected_types": ["copy", "=", "id", ";"],
        },
        {
            "code": 'a = b ** c;',
            "expected_types": ["id", "=", "id", "Invalid Lexeme", "Invalid Character", "id", ";"],
        },
        {
            "code": '#notacomment;',
            "expected_types": ["Invalid Lexeme", "Invalid Character", "id", ";"],
        },
        {
            "code": """m{
n}
o"
""",
            "expected_types": ["Invalid Lexeme", "Invalid Character", "Invalid Lexeme", "Invalid Character","Invalid Lexeme", "Invalid Character"],
        },
        {
            "code": 'B# ',
            "expected_types": ["id", "comment_single"],
        },
        {
            "code": '3*287',
            "expected_types": ["piece_lit", "*", "piece_lit"],
        },
        {
            "code": 'long_id_long_id_long_id_long_id_long_id',
            "expected_types": [Token.ExceedsLimit],
        },
        {
            "code": '123456789123456789.1234567',
            "expected_types": [Token.ExceedsLimit],
        },
        {
            "code": '123456789123456.12345678',
            "expected_types": [Token.ExceedsLimit],
        },
        {
            "code": '12345678912345.1234567',
            "expected_types": ["sip_lit"],
        },
        {
            "code": '213123dasdsd',
            "expected_types": [Token.InvalidLexeme, Token.InvalidCharacter, "id"],
        },
        {
            "code": '0',
            "expected_types": ["piece_lit"],
        },
    ]

    def test_strings(self):
        for i, case in enumerate(self.string_tests, 1):
            with self.subTest(case=i):
                lexer = Lexer(case["code"])
                tokens = [t for t in lexer.tokenize() if t.type not in ("comment", "space", "newline", "tab")]
                actual_types = [t.type for t in tokens]
                self.assertEqual(actual_types, case["expected_types"], msg=f"\nFAILED ON CODE:\n----------\n{case['code']}\n----------")


if __name__ == "__main__":
    unittest.main()
