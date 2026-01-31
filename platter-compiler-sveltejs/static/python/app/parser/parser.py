from app.lexer.lexer import Lexer
from app.parser.error_handler import ErrorHandler


class Parser():
    def __init__(self, tokens):
        self.tokens = [t for t in tokens if t.type not in ("space", "tab", "newline", "comment_single", "comment_multi")] # filter out ws and comments
        if not self.tokens: 
            raise ErrorHandler("Parse_err", None, "start")  # replace start with program predict set
        else: pass
            # parse(self.tokens)
    
    def parse(self):
        # TODO: Implement parsing logic
        return True

if __name__ == "__main__":
    from app.utils.FileHandler import run_file
    
    filename = "parser.platter"
    code = run_file(filename)
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    try:
        if parser.parse(): print("Syntax OK")
    except SyntaxError as e:
        print(str(e))