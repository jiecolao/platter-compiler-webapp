import os
from app.lexer.lexer import Lexer
from app.parser.parser import Parser
from tests.syntax_tscripts import SYNTAX_TSCRIPTS

class TestParser():
    
    def run_script(self):
        # choice = input("Enter test script number: ").strip()
        for script in SYNTAX_TSCRIPTS:
            msg = (
                f"============ CODE #{script['number']} ================\n"
                f"ACTUAL OUTPUT: {script['actual_output']}\n"
                f"CODE:\n{script['code']}\n"
                f"=====================================\n"
            )
            # turn off log errors
            code = script["code"]
            lexer = Lexer(code)
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            
            try:
                parser.parse()
                print("No Syntax Error")
            except SyntaxError as e:
                print(str(e))
                
            print(msg)

if __name__=="__main__":
    tester = TestParser()
    tester.run_script()