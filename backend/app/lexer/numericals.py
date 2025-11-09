from app.lexer.protocol import LexerProtocol
from app.lexer.token import Token


class LexerNumericals(LexerProtocol):
    def s_num_start(self):
        # This function implements the logic of the FA for piece/sip literals.
        # It's implemented iteratively to respect the 15-whole and 7-decimal limit.

        whole_digits = 0
        token_type = "piece_lit"

        if self.current == "-":
            self.advance()  # Consume '-'

        # Must have at least one digit after '-'
        if self.current is None or self.current not in self.DIGITS:
            return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

        # Consume up to 15 whole digits
        while self.current in self.DIGITS:
            if whole_digits >= 15:
                self.advance()  # Consume the 16th+ digit
                return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)
            self.advance()
            whole_digits += 1

        # Check for decimal part
        if self.current == ".":
            token_type = "sip_lit"
            self.advance()  # Consume '.'
            decimal_digits = 0

            # Must have at least one digit after '.'
            if self.current is None or self.current not in self.DIGITS:
                return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

            while self.current in self.DIGITS:
                if decimal_digits >= 7:
                    self.advance()  # Consume the 8th+ decimal
                    return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)
                self.advance()
                decimal_digits += 1

        # End of number (piece_lit or sip_lit)
        if self._match_delimiter(self.num_delim):
            return Token(token_type, self.get_lexeme(), self.start_line, self.start_col)

        # Invalid delimiter
        self.advance()  # Consume the offending character
        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)