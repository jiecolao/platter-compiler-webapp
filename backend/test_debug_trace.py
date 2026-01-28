from app.parser.parser import Parser
from app.lexer.lexer import Lexer

code = 'start(){ bill(tochars(topiece("123"))); }'

lexer = Lexer(code)
tokens = lexer.tokenize()

# Patch the parser to add debug output
original_tail1 = Parser.tail1
def debug_tail1(self):
    print(f"  tail1 called, current_tok = '{self.current_tok}'")
    result = original_tail1(self)
    print(f"  tail1 returning: {result}")
    return result

original_call_tail = Parser.call_tail
def debug_call_tail(self):
    print(f"    call_tail called, current_tok = '{self.current_tok}'")
    result = original_call_tail(self)
    print(f"    call_tail returning: {result} (length: {len(result) if result else 0})")
    return result

original_flavor = Parser.flavor
def debug_flavor(self):
    print(f"      flavor called, current_tok = '{self.current_tok}'")
    result = original_flavor(self)
    print(f"      flavor returning: {result} (length: {len(result) if result else 0})")
    return result

Parser.tail1 = debug_tail1
Parser.call_tail = debug_call_tail
Parser.flavor = debug_flavor

parser = Parser([t for t in tokens])
ast = parser.parse()

if ast.start_platter and ast.start_platter.statements:
    stmt = ast.start_platter.statements[0]
    if hasattr(stmt, 'recipe_call'):
        rc = stmt.recipe_call
        print(f'\n=== RESULT ===')
        print(f'RecipeCall: {rc.recipe_name}')
        print(f'Arguments: {rc.arguments}')
        print(f'Length: {len(rc.arguments)}')
