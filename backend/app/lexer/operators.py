from app.lexer.token import Token
from app.lexer.protocol import LexerProtocol


class LexerOperators(LexerProtocol):

    def s201(self):  # + (Accepting State 202)
        self.advance()
        if self.current == "=": return self.s203()
        if self._match_delimiter(self.op1_dlm):
            return Token("+", "+", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s203(self):  # += (Accepting State 204)
        self.advance()
        if self._match_delimiter(self.op1_dlm):
            return Token("+=", "+=", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s205(self):  # - (Accepting State 206)
        self.advance()
        if self.current == "=": return self.s207()
        if self._match_delimiter(self.op2_dlm):
            return Token("-", "-", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s207(self):  # -= (Accepting State 208)
        self.advance()
        if self._match_delimiter(self.op1_dlm):
            return Token("-=", "-=", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s209(self):  # * (Accepting State 210)
        self.advance()
        if self.current == "=": return self.s211()
        if self._match_delimiter(self.op1_dlm):
            return Token("*", "*", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s211(self):  # *= (Accepting State 212)
        self.advance()
        if self._match_delimiter(self.op1_dlm):
            return Token("*=", "*=", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s213(self):  # / (Accepting State 214)
        self.advance()
        if self.current == "=": return self.s215()
        if self._match_delimiter(self.op1_dlm):
            return Token("/", "/", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s215(self):  # /= (Accepting State 216)
        self.advance()
        if self._match_delimiter(self.op1_dlm):
            return Token("/=", "/=", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s217(self):  # % (Accepting State 218)
        self.advance()
        if self.current == "=": return self.s219()
        if self._match_delimiter(self.op1_dlm):
            return Token("%", "%", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s219(self):  # %= (Accepting State 220)
        self.advance()
        if self._match_delimiter(self.op1_dlm):
            return Token("%=", "%=", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s221(self):  # > (Accepting State 222)
        self.advance()
        if self.current == "=": return self.s223()
        if self._match_delimiter(self.op1_dlm):
            return Token(">", ">", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s223(self):  # >= (Accepting State 224)
        self.advance()
        if self._match_delimiter(self.op1_dlm):
            return Token(">=", ">=", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s225(self):  # < (Accepting State 226)
        self.advance()
        if self.current == "=": return self.s227()
        if self._match_delimiter(self.op1_dlm):
            return Token("<", "<", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s227(self):  # <= (Accepting State 228)
        self.advance()
        if self._match_delimiter(self.op1_dlm):
            return Token("<=", "<=", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s229(self):  # = (Accepting State 230)
        self.advance()
        if self.current == "=": return self.s231()
        if self._match_delimiter(self.equal_dlm):
            return Token("=", "=", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s231(self):  # == (Accepting State 232)
        self.advance()
        if self._match_delimiter(self.op1_dlm):
            return Token("==", "==", self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)
