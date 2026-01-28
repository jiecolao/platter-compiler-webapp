from app.parser.parser import Parser
from app.lexer.lexer import Lexer
from app.semantic_analyzer.ast_reader import ASTReader

code = '''chars[] of names = ["Hello Platter", "Raph", "Jieco"];

start() {
}'''

lexer = Lexer(code)
tokens = lexer.tokenize()
parser = Parser([t for t in tokens])
ast = parser.parse()

reader = ASTReader(ast)
print(reader.read())
