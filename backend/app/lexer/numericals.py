from app.lexer.protocol import LexerProtocol
from app.lexer.token import Token


class LexerNumericals(LexerProtocol):


    def s298(self):  # -
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s303(self):  # . (Decimal point)
        self.advance()
        if self.current in self.NUMERIC: return self.s331()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    # --- Whole Digits (s301 to s330) ---

    def s301(self):  # Digit 1
        self.advance()
        if self.current in self.NUMERIC: return self.s304()
        if self.current == ".": return self.s303()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s304(self):  # Digit 2
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s306()
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s306(self):  # Digit 3
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s308()
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s308(self):  # Digit 4
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s310()
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s310(self):  # Digit 5
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s312()
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s312(self):  # Digit 6
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s314()
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s314(self):  # Digit 7
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s316()
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s316(self):  # Digit 8
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s318()
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s318(self):  # Digit 9
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s320()
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s320(self):  # Digit 10
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s322()
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s322(self):  # Digit 11
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s324()
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s324(self):  # Digit 12
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s326()
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s326(self):  # Digit 13
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s328()
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s328(self):  # Digit 14
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s330()
        if self.current == ".": return self.s303()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s330(self):  # Digit 15 (Max whole digits)
        self.advance()
        # If 16th digit appears, it's invalid as per original loop constraint
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC:
            # Consume all remaining digits recursively then return invalid
            return self._consume_invalid_numerical()
        if self.current == ".": return self.s303()
        return [Token(Token.ExceedsLimit, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    # --- Decimal Digits (s331 to s343) ---

    def s331(self):  # Decimal Digit 1
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s333()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s333(self):  # Decimal Digit 2
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s335()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s335(self):  # Decimal Digit 3
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s337()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s337(self):  # Decimal Digit 4
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s339()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s339(self):  # Decimal Digit 5
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s341()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s341(self):  # Decimal Digit 6
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.NUMERIC: return self.s343()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s343(self):  # Decimal Digit 7 (Max decimal digits)
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        # If 8th decimal digit appears, it's invalid - consume all remaining digits
        if self.current in self.NUMERIC:
            return self._consume_invalid_numerical()
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def _consume_invalid_numerical(self):
        """Recursively consume all remaining digits and decimal points, then return InvalidLexeme."""
        self.advance()
        # Continue consuming digits or decimal points
        if self.current is not None and self.current in self.NUMERIC or self.current == ".":
            return self._consume_invalid_numerical()
        # Once we hit a non-digit/non-decimal, return invalid lexeme
        return Token(Token.ExceedsLimit, self.get_lexeme(), self.start_line, self.start_col)
