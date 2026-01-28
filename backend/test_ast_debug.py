from app.parser.parser import Parser
from app.lexer.lexer import Lexer
from app.semantic_analyzer.ast_reader import ASTReader

code = '''start(){
bill(tochars(topiece("123")));
}'''

lexer = Lexer(code)
tokens = lexer.tokenize()
parser = Parser([t for t in tokens])
ast = parser.parse()

print('AST Type:', type(ast))
print('Start Platter:', ast.start_platter)

if ast.start_platter and ast.start_platter.statements:
    stmt = ast.start_platter.statements[0]
    print('First statement type:', type(stmt).__name__)
    
    if hasattr(stmt, 'recipe_call'):
        rc = stmt.recipe_call
        print('Recipe call:', rc)
        print('Recipe name:', rc.recipe_name)
        print('Arguments:', rc.arguments)
        print('Arguments length:', len(rc.arguments))
        
        if rc.arguments:
            print('\nFirst argument:', rc.arguments[0])
            print('First argument type:', type(rc.arguments[0]).__name__)

print('\n\n=== AST Reader Output ===')
reader = ASTReader(ast)
print(reader.read())
