from app.parser.parser import Parser
from app.lexer.lexer import Lexer
from app.semantic_analyzer.ast_reader import ASTReader

code = '''start(){
bill(tochars(topiece("3245")+topiece("13245")));
}'''

lexer = Lexer(code)
tokens = lexer.tokenize()
parser = Parser([t for t in tokens])
ast = parser.parse()

reader = ASTReader(ast)
print(reader.read())
