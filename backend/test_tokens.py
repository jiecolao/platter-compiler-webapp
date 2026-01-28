from app.parser.parser import Parser
from app.lexer.lexer import Lexer
import logging

# Enable debug logging
logging.basicConfig(level=logging.INFO)

code = '''start(){
bill(tochars(topiece("123")));
}'''

lexer = Lexer(code)
tokens = lexer.tokenize()

print("=== TOKENS ===")
for t in tokens:
    print(f"{t.type}: {t.value}")

print("\n=== PARSING ===")
parser = Parser([t for t in tokens])
ast = parser.parse()

print("\n=== RESULT ===")
if ast.start_platter and ast.start_platter.statements:
    stmt = ast.start_platter.statements[0]
    if hasattr(stmt, 'recipe_call'):
        rc = stmt.recipe_call
        print(f'RecipeCall: {rc.recipe_name}')
        print(f'Arguments count: {len(rc.arguments)}')
        print(f'Arguments: {rc.arguments}')
