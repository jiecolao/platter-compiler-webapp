from pprint import pprint
import unittest
import os
import subprocess
from app.lexer.lexer import Lexer
from tests.syntax_tscripts import SYNTAX_TSCRIPTS

samples_dir = "./tests/parser_programs/"

def run_():
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
    for t in tokens:
        print(t)
    # print("\n\nTOKENS:")
    # pprint(tokens)
    self.set_clipboard(("\n".join(t.type for t in tokens)))
    

def run_file(filename):
    filepath = os.path.join(samples_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()
        return source

def run_all_files():
    platter_files = [f for f in os.listdir(samples_dir) if f.endswith(".platter") or f.endswith(".draft")]
    for filename in platter_files:
        filepath = os.path.join(samples_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()
            lexer = Lexer(source)
            tokens = lexer.tokenize()