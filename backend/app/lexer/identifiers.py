from app.lexer.token import Token
from app.lexer.protocol import LexerProtocol


class LexerIdentifier(LexerProtocol):
    def s248(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s249()
        if self.current in self.id_chars: return self.s250()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s249(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s250(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s251()
        if self.current in self.id_chars: return self.s252()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s251(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s252(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s253()
        if self.current in self.id_chars: return self.s254()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s253(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s254(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s255()
        if self.current in self.id_chars: return self.s256()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s255(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s256(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s257()
        if self.current in self.id_chars: return self.s258()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s257(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s258(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s259()
        if self.current in self.id_chars: return self.s260()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s259(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s260(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s261()
        if self.current in self.id_chars: return self.s262()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s261(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s262(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s263()
        if self.current in self.id_chars: return self.s264()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s263(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s264(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s265()
        if self.current in self.id_chars: return self.s266()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s265(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s266(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s267()
        if self.current in self.id_chars: return self.s268()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s267(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s268(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s269()
        if self.current in self.id_chars: return self.s270()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s269(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s270(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s271()
        if self.current in self.id_chars: return self.s272()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s271(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s272(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s273()
        if self.current in self.id_chars: return self.s274()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s273(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s274(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s275()
        if self.current in self.id_chars: return self.s276()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s275(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s276(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s277()
        if self.current in self.id_chars: return self.s278()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s277(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s278(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s279()
        if self.current in self.id_chars: return self.s280()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s279(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s280(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s281()
        if self.current in self.id_chars: return self.s282()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s281(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s282(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s283()
        if self.current in self.id_chars: return self.s284()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s283(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s284(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s285()
        if self.current in self.id_chars: return self.s286()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s285(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s286(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s287()
        if self.current in self.id_chars: return self.s288()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s287(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s288(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s289()
        if self.current in self.id_chars: return self.s290()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s289(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s290(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s291()
        if self.current in self.id_chars: return self.s292()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s291(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s292(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s293()
        if self.current in self.id_chars: return self.s294()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s293(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s294(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s295()
        if self.current in self.id_chars: return self.s296()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s295(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)

    def s296(self):
        self.advance()
        if self._match_delimiter(self.id_delim): return self.s297()
        if self.current in self.id_chars:  return Token(Token.InvalidLexemeExceeds, self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s297(self):
        return Token("id", self.get_lexeme(), self.start_line, self.start_col)