import os
from app.lexer.lexer import Lexer
from app.parser.parser import Parser
from tests.syntax_tscripts import SYNTAX_TSCRIPTS

class TestParser():

    def run_script(self):
        # choice = input("Enter test script number: ").strip()
        for script in SYNTAX_TSCRIPTS:
            code = script["code"]
            lexer = Lexer(code)
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            result = ""

            try:
                result = parser.parse()
                msg = (
                    f"============ CODE #{script['number']} ================\n"
                    f"CODE:\n{script['code']}\n"
                    f"EXPECTED OUTPUT: {script['expected_output']}\n"
                    f"SYNTAX OUTPUT: {"✔ No Syntax Error" if result else None}\n"
                    f"=====================================\n"
                )
            except SyntaxError as e:
                msg = (
                    f"============ CODE #{script['number']} ================\n"
                    f"CODE:\n{script['code']}\n"
                    f"EXPECTED OUTPUT: {script['expected_output']}\n"
                    f"SYNTAX OUTPUT: {e}\n"
                    f"=====================================\n"
                )
            
            print(msg)

if __name__=="__main__":
    tester = TestParser()
    tester.run_script()