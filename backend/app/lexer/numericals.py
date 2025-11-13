from app.lexer.protocol import LexerProtocol
from app.lexer.token import Token


class LexerNumericals(LexerProtocol):


    def s298(self):  # -
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s299()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s299(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s300(self):  # Digit 1
        self.advance()
        if self.current in self.numeric: return self.s303()
        if self.current == ".": return self.s302()
        if self._match_delimiter(self.num_delim): return self.s301()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s301(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s302(self):  # . (Decimal point)
        self.advance()
        if self.current in self.numeric: return self.s331()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s303(self):  # Digit 2
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s304()
        if self.current in self.numeric: return self.s305()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s304(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s305(self):  # Digit 3
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s306()
        if self.current in self.numeric: return self.s307()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s306(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s307(self):  # Digit 4
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s308()
        if self.current in self.numeric: return self.s309()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s308(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s309(self):  # Digit 5
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s310()
        if self.current in self.numeric: return self.s311()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s310(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s311(self):  # Digit 6
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s312()
        if self.current in self.numeric: return self.s313()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s312(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s313(self):  # Digit 7
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.numeric: return self.s315()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s315(self):  # Digit 8
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s316()
        if self.current in self.numeric: return self.s317()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s316(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s317(self):  # Digit 9
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s318()
        if self.current in self.numeric: return self.s319()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s318(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s319(self):  # Digit 10
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s320()
        if self.current in self.numeric: return self.s321()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s320(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s321(self):  # Digit 11
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s322()
        if self.current in self.numeric: return self.s323()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s322(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s323(self):  # Digit 12
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s324()
        if self.current in self.numeric: return self.s325()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s324(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s325(self):  # Digit 13
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s326()
        if self.current in self.numeric: return self.s327()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s326(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s327(self):  # Digit 14
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s328()
        if self.current in self.numeric: return self.s329()
        if self.current == ".": return self.s302()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s328(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s329(self):  # Digit 15 (Max whole digits)
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s330()
        if self.current in self.numeric: return self._consume_invalid_numerical()
        if self.current == ".": return self.s302()
        return [Token(Token.ExceedsLimit, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s330(self):
        return Token("piece_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s331(self):  # Decimal Digit 1
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s332()
        if self.current in self.numeric: return self.s333()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s332(self):
        return Token("sip_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s333(self):  # Decimal Digit 2
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s334()
        if self.current in self.numeric: return self.s335()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s334(self):
        return Token("sip_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s335(self):  # Decimal Digit 3
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s336()
        if self.current in self.numeric: return self.s337()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s336(self):
        return Token("sip_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s337(self):  # Decimal Digit 4
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s338()
        if self.current in self.numeric: return self.s339()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s338(self):
        return Token("sip_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s339(self):  # Decimal Digit 5
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s340()
        if self.current in self.numeric: return self.s341()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s340(self):
        return Token("sip_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s341(self):  # Decimal Digit 6
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s342()
        if self.current in self.numeric: return self.s343()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s342(self):
        return Token("sip_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def s343(self):  # Decimal Digit 7 (Max decimal digits)
        self.advance()
        if self._match_delimiter(self.num_delim): return self.s344()
        if self.current in self.numeric: return self._consume_invalid_numerical()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s344(self):
        return Token("sip_lit", self.get_lexeme(), self.start_line,
                     self.start_col)

    def _consume_invalid_numerical(self):
        """Recursively consume all remaining digits and decimal points, then return InvalidLexeme."""
        self.advance()
        if self.current is not None and self.current in self.numeric or self.current == ".":
            return self._consume_invalid_numerical()
        return Token(Token.ExceedsLimit, self.get_lexeme(), self.start_line, self.start_col)
