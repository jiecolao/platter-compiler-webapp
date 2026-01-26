from app.lexer.token import Token
from app.lexer.protocol import LexerProtocol


class LexerCharCom(LexerProtocol):

    def s345(self):
        self.advance()
        if self.current is None: return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

        if self.current in self.ascii_1: return self.s345()
        if self.current == '\\': return self.s346()
        if self.current == '"': return self.s347()

        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s346(self):
        self.advance()
        if self.current is None: return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)
        if self.current in self.ascii: return self.s345()

        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s347(self):
        self.advance()
        return Token("chars_lit", self.get_lexeme(), self.start_line, self.start_col)

    def s348(self):
        self.advance()
        if self.current == ' ': return self.s349()
        if self.current == '#': return self.s351()

        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)]

    def s349(self):
        self.advance()
        if self.current in self.ascii_2: return self.s349()
        if self.current == '\n': return self.s350()
        if self.current is None: return self.s350()

        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)]

    def s350(self):
        return Token("comment_single", self.get_lexeme(), self.start_line, self.start_col)

    def s351(self):
        self.advance()
        if self.current is None: return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)
        if self.current == '#': return self.s352()

        return self.s351()

    def s352(self):
        self.advance()
        if self.current is None: return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)
        if self.current == '#': return self.s353()

        return self.s351()

    def s353(self):
        self.advance()
        return Token("comment_multi", self.get_lexeme(), self.start_line, self.start_col)
