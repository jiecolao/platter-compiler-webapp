from pprint import pprint
import os
from app.lexer.lexer import Lexer
import subprocess

def set_clipboard(text: str):
    subprocess.run("clip", universal_newlines=True, input=text)


samples_dir = "./tests/lexer_programs/"

choice = input("Include whitespace tokens (y/n)? ").lower().strip()
include_whitespace = choice == 'y'

platter_files = [f for f in os.listdir(samples_dir) if f.endswith(".platter") or f.endswith(".draft")]

print(f"\nFiles in {samples_dir}:")
for i, f in enumerate(platter_files, 1):
    print(f" {i}. {f}")

index = int(input("\nEnter file index from above: ").strip())
filename = platter_files[index - 1]
filepath = os.path.join(samples_dir, filename)

with open(filepath, "r", encoding="utf-8") as f:
    source = f.read()

lexer = Lexer(source)
tokens = lexer.tokenize()

tokens = [
    t for t in tokens
    if t.type not in ("comment", "space", "newline", "tab") or include_whitespace
]

print("\n\nTOKENS:")
pprint(tokens)
set_clipboard(("\n".join(t.type for t in tokens)))
