from app.lexer.lexer import Lexer
from app.lexer.token import Token
from pprint import pprint

# pede gumamit lark

class ASTNode:
    def __init__(self, node_type, value=None, children=None):
        self.node_type = node_type
        self.value = value
        self.children = children or []

    def __repr__(self):
        if self.children:
            return f"{self.node_type}({self.children})"
        return f"{self.node_type}({self.value})"


class Parser:
    def __init__(self, tokens):
        self.tokens = [t for t in tokens if t.type not in ("space", "newline", "tab", "comment")]
        self.pos = 0
        self.current = self.tokens[self.pos] if self.tokens else None

    def advance(self):
        self.pos += 1
        self.current = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def expect(self, token_type):
        """Consume the token if it matches, otherwise raise error."""
        if self.current is None:
            raise SyntaxError(f"Expected {token_type}, got EOF")
        if self.current.type != token_type:
            raise SyntaxError(f"Expected {token_type}, got {self.current.type}")
        value = self.current.value
        self.advance()
        return value

    # Example: parsing a simple variable assignment: piece x = 5;
    def parse_assignment(self):
        children = []

        # Expect 'piece' keyword
        children.append(ASTNode("Keyword", self.expect("piece")))

        # Expect identifier
        children.append(ASTNode("Identifier", self.expect("id")))

        # Expect '=' operator
        children.append(ASTNode("Operator", self.expect("=")))

        # Expect literal (number or string)
        if self.current.type in ("piece_lit", "num", "string"):
            children.append(ASTNode("Literal", self.current.value))
            self.advance()
        else:
            raise SyntaxError(f"Expected literal, got {self.current.type}")

        # Expect semicolon
        children.append(ASTNode("Terminator", self.expect(";")))

        return ASTNode("Assignment", children=children)

    def parse(self):
        """Entry point for parsing. Returns AST."""
        ast = []
        while self.current:
            if self.current.type == "piece":
                ast.append(self.parse_assignment())
            else:
                raise SyntaxError(f"Unexpected token {self.current.type}")
        return ast

# Example usage:
code = 'piece x = 5;'
lexer = Lexer(code)
tokens = lexer.tokenize()
# pprint(tokens)
parser = Parser(tokens)
ast = parser.parse()
print(ast)