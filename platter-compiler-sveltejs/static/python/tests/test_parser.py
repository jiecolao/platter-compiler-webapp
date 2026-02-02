from app.lexer.lexer import Lexer
from app.parser.parser_program import Parser
from tests.syntax_tscripts import SYNTAX_TSCRIPTS
import os

class TestParser():

    def msg(self, num, code, exp_outp, act_outp, result, file):
        message = (
            f"============ CODE #{num} ================\n"
            f"CODE:\n{code}\n"
            f"EXPECTED OUTPUT: {exp_outp}\n"
            f"ACTUAL OUTPUT: {act_outp}\n"
            f"SYNTAX OUTPUT: {result}\n"
            f"=====================================\n\n"
        )
        file.write(message)

    def run_script(self):
        # Get the directory of this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_file = os.path.join(script_dir, "test_parser_output.txt")
        
        with open(output_file, 'w') as f:
            for script in SYNTAX_TSCRIPTS:
                lexer = Lexer(script["code"])
                tokens = lexer.tokenize()
                parser = Parser(tokens)
                result = ""

                try:
                    result = parser.parse_program()
                    self.msg(script["number"], 
                             script["code"], 
                             script["expected_output"], 
                             script["actual_output"],
                             "Syntax OK" if result else None,
                             f)

                except SyntaxError as e:
                    self.msg(script["number"], 
                             script["code"], 
                             script["expected_output"], 
                             script["actual_output"],
                             e,
                             f)
        
        print(f"Output written to {output_file}")

if __name__=="__main__":
    tester = TestParser()
    tester.run_script()