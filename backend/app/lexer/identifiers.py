from app.lexer.token import Token
from app.lexer.protocol import LexerProtocol


class LexerIdentifier(LexerProtocol):

    def s248(self, count=1):  # The start of an identifier (alpha or _)
        self.advance()

        if count < 25 and self.current is not None and self.current in self.ID_BODY:
            return self.s248(count + 1)

        if self._match_delimiter(self.id_delim):
            return Token("id", self.get_lexeme(), self.start_line, self.start_col)

        return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)
