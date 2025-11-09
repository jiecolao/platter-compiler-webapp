
from pprint import pprint
import os
print(os.getcwd())

from app.lexer.lexer import Lexer

includeWhitespace = False
with open("./tests/sample_programs/lexer_2.platter", "r", encoding="utf-8") as f:
    source = f.read()

lexer = Lexer(source)
tokens = lexer.tokenize()

if not includeWhitespace: tokens = [n for n in tokens if n.type not in ("space", "newline", "tab")]

print("\n\nTOKENS:")
pprint(tokens, indent=4, width=80)