from app.lexer.token import Token
from app.lexer.protocol import LexerProtocol


class LexerCharCom(LexerProtocol):

    def s345(self):  # Inside string after initial '"'
        if self.current is None:
            return Token("UNKNOWN", self.get_lexeme(), self.start_line, self.start_col)

        if self.current == '"':  # State 347
            self.advance()  # Consume closing '"'
            return Token("chars_lit", self.get_lexeme(), self.start_line, self.start_col)

        if self.current == '\\':  # Escape sequence
            self.advance()  # Consume '\'
            return self.s346()

        # Regular character (ascii_1 loop)
        # Check for invalid characters (like newline)
        if self.current == '\n':
            return Token("UNKNOWN", self.get_lexeme(), self.start_line, self.start_col)

        self.advance()
        return self.s345()

    def s346(self):  # After '\' (Expects any ascii character)
        if self.current is None:
            return Token("UNKNOWN", self.get_lexeme(), self.start_line, self.start_col)

        # Consume the escaped character (any char is ok, incl. '"' or 'n')
        self.advance()
        return self.s345()  # Back to the main string state

    def s348(self):  # After initial '#'
        if self.current == '#':  # Start of multi-line comment (##)
            self.advance()  # Consume second '#'
            return self.s351()  # State 351 (Inside multiline comment)

        if self.current == ' ':
            self.advance()
            return self.s349()

        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

    def s349(self):
        while self.current is not None and self.current != '\n':
            self.advance()

        if self.current is None:  # EOF
            return Token("comment_single", self.get_lexeme(), self.start_line, self.start_col)

        # State 350 (Accepting)
        if self.current == '\n':
            self.advance()  # Consume the newline

        return Token("comment_single", self.get_lexeme(), self.start_line, self.start_col)

    def s351(self):  # Inside multi-line comment (## ... )
        if self.current is None:  # EOF
            return Token("UNKNOWN", self.get_lexeme(), self.start_line, self.start_col)

        if self.current == '#':
            self.advance()  # Consume first '#'
            return self.s352()  # Potential closing '##'

        self.advance()  # Loop on ascii_3
        return self.s351()

    def s352(self):  # After first '#' inside multi-line comment (## ... #)
        if self.current is None:  # EOF
            return Token("UNKNOWN", self.get_lexeme(), self.start_line, self.start_col)

        if self.current == '#':
            self.advance()  # Consume second '#'
            # State 353 (Accepting State)
            return Token("comment_multi", self.get_lexeme(), self.start_line, self.start_col)

        # Not a '##', go back to general consumption
        return self.s351()
