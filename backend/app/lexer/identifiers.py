from app.lexer.token import Token
from app.lexer.protocol import LexerProtocol


class LexerIdentifier(LexerProtocol):
    def s248(self):  # After 1 char
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s250()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]

        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s250(self):  # After 2 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s252()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s252(self):  # After 3 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s254()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s254(self):  # After 4 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s256()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s256(self):  # After 5 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s258()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s258(self):  # After 6 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s260()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s260(self):  # After 7 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s262()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s262(self):  # After 8 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s264()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s264(self):  # After 9 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s266()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s266(self):  # After 10 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s268()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s268(self):  # After 11 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s270()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s270(self):  # After 12 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s272()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s272(self):  # After 13 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s274()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s274(self):  # After 14 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s276()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s276(self):  # After 15 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s278()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s278(self):  # After 16 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s280()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s280(self):  # After 17 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s282()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s282(self):  # After 18 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s284()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s284(self):  # After 19 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s286()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s286(self):  # After 20 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s288()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s288(self):  # After 21 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s290()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s290(self):  # After 22 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s292()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s292(self):  # After 23 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s294()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s294(self):  # After 24 chars
        if self.current is not None and self.current in self.ID_BODY:
            self.advance()
            return self.s296()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s296(self):  # After 25 chars (MAX)
        # This is the last valid character.
        # If another ID_BODY char appears, it's an error (too long).
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line,
                                                             self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)

        # If we are here, it's either an invalid delimiter OR
        # another ID_BODY char (making it 26+). Both are invalid.
        while self.current is not None and self.current in self.ID_BODY:
            self.advance()
        return [Token(Token.ExceedsLimit, self.get_lexeme(), self.start_line, self.start_col)]