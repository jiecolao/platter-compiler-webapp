from app.lexer.protocol import LexerProtocol
from app.lexer.token import Token


class LexerNumericals(LexerProtocol):

    def s_num_start(self):
        # Entry point (State 0)
        if self.current == "-": return self.s298()
        if self.current in self.DIGITS: return self.s301()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s298(self):  # -
        self.advance()
        if self.current in self.DIGITS: return self.s301()
        # Transition to s300 (error state for -.) in image, or generic invalid
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s303(self):  # . (Decimal point)
        self.advance()
        if self.current in self.DIGITS: return self.s331()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    # --- Whole Digits (s301 to s330) ---

    def s301(self):  # Digit 1
        self.advance()
        if self.current in self.DIGITS: return self.s304()
        if self.current == ".": return self.s303()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s304(self):  # Digit 2
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s306()
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s306(self):  # Digit 3
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s308()
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s308(self):  # Digit 4
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s310()
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s310(self):  # Digit 5
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s312()
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s312(self):  # Digit 6
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s314()
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s314(self):  # Digit 7
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s316()
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s316(self):  # Digit 8
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s318()
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s318(self):  # Digit 9
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s320()
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s320(self):  # Digit 10
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s322()
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s322(self):  # Digit 11
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s324()
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s324(self):  # Digit 12
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s326()
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s326(self):  # Digit 13
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s328()
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s328(self):  # Digit 14
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s330()
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s330(self):  # Digit 15 (Max whole digits)
        self.advance()
        # If 16th digit appears, it's invalid as per original loop constraint
        if self._match_delimiter(self.num_delim): return Token("piece_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS:
            self.advance()  # Consume the invalid extra digit
            return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)
        if self.current == ".": return self.s303()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    # --- Decimal Digits (s331 to s343) ---

    def s331(self):  # Decimal Digit 1
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s333()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s333(self):  # Decimal Digit 2
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s335()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s335(self):  # Decimal Digit 3
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s337()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s337(self):  # Decimal Digit 4
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s339()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s339(self):  # Decimal Digit 5
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s341()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s341(self):  # Decimal Digit 6
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        if self.current in self.DIGITS: return self.s343()
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s343(self):  # Decimal Digit 7 (Max decimal digits)
        self.advance()
        if self._match_delimiter(self.num_delim): return Token("sip_lit", self.get_lexeme(), self.start_line,
                                                               self.start_col)
        # If 8th decimal digit appears, it's invalid
        if self.current in self.DIGITS:
            self.advance()
            return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)