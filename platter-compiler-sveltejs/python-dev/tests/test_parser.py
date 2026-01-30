from app.lexer.lexer import Lexer
from app.parser.parser import Parser
from tests.syntax_tscripts import SYNTAX_TSCRIPTS

class TestParser():

    def msg(self, num, code, exp_outp, act_outp, result):
        print(
            f"============ CODE #{num} ================\n"
            f"CODE:\n{code}\n"
            f"EXPECTED OUTPUT: {exp_outp}\n"
            f"ACTUAL OUTPUT: {act_outp}\n"
            f"SYNTAX OUTPUT: {result}\n"
            f"=====================================\n"
        )

    def run_script(self):
        # choice = input("Enter test script number: ").strip()
        for script in SYNTAX_TSCRIPTS:
            lexer = Lexer(script["code"])
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            result = ""

            try:
                result = parser.parse()
                self.msg(script["number"], 
                         script["code"], 
                         script["expected_output"], 
                         script["actual_output"],
                         "Syntax OK" if result else None)

            except SyntaxError as e:
                self.msg(script["number"], 
                         script["code"], 
                         script["expected_output"], 
                         script["actual_output"],
                         e)

if __name__=="__main__":
    tester = TestParser()
    tester.run_script()