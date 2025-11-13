from app.lexer.token import Token
from app.lexer.protocol import LexerProtocol


class LexerIdentifier(LexerProtocol):
    def s248(self):
        if self.current in self.id_chars: return self.s250()
        return self.s249()
    
    def s249(self):
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s250(self):
        self.advance()
        if self.current in self.id_chars: return self.s252()
        return self.s253()
    
    def s253(self):
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s252(self):
        self.advance()
        if self.current in self.id_chars: return self.s254()
        return self.s257()
    
    def s257(self):  # Accepting state for 3 chars
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s254(self):
        self.advance()
        if self.current in self.id_chars: return self.s256()
        return self.s261()
    
    def s261(self):  # Accepting state for 4 chars
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s256(self):
        self.advance()
        if self.current in self.id_chars: return self.s258()
        return self.s265()
    
    def s265(self):
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s258(self):
        self.advance()
        if self.current in self.id_chars: return self.s260()
        return self.s269()
    
    def s269(self): 
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s260(self):
        self.advance()
        if self.current in self.id_chars: return self.s262()
        return self.s273()
    
    def s273(self):  # Accepting state for 7 chars
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s262(self):
        self.advance()
        if self.current in self.id_chars: return self.s264()
        return self.s277()
    
    def s277(self):  # Accepting state for 8 chars
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s264(self):
        self.advance()
        if self.current in self.id_chars: return self.s266()
        return self.s281()
    
    def s281(self):  # Accepting state for 9 chars
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s266(self):
        self.advance()
        if self.current in self.id_chars: return self.s268()
        return self.s285()
    
    def s285(self):  # Accepting state for 10 chars
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s268(self):
        self.advance()
        if self.current in self.id_chars: return self.s270()
        return self.s289()
    
    def s289(self):  # Accepting state for 11 chars
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s270(self):
        self.advance()
        if self.current in self.id_chars: return self.s272()
        return self.s293()
    
    def s293(self):  # Accepting state for 12 chars
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s272(self):
        self.advance()
        if self.current in self.id_chars: return self.s274()
        return self.s297()
    
    def s297(self):  # Accepting state for 13 chars
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s274(self):
        self.advance()
        if self.current in self.id_chars: return self.s276()
        return self.s278()
    
    def s278(self):  # Accepting state for 14 chars
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s276(self):
        self.advance()
        if self.current in self.id_chars: return self.s280()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s280(self):
        self.advance()
        if self.current in self.id_chars: return self.s282()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s282(self):
        self.advance()
        if self.current in self.id_chars: return self.s284()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s284(self):
        self.advance()
        if self.current in self.id_chars: return self.s286()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s286(self):
        self.advance()
        if self.current in self.id_chars: return self.s288()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s288(self):
        self.advance()
        if self.current in self.id_chars: return self.s290()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s290(self):
        self.advance()
        if self.current in self.id_chars: return self.s292()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s292(self):
        self.advance()
        if self.current in self.id_chars: return self.s294()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s294(self):
        self.advance()
        if self.current in self.id_chars: return self.s296()
        if self.get_lexeme() in self.KEYWORDS: return [Token(Token.InvalidIdentifier, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]
        if self._match_delimiter(self.id_delim): return Token("id", self.get_lexeme(), self.start_line, self.start_col)
        return [Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col), self._error_invalid_char()]

    def s296(self):
        self.advance()
        while self.current is not None and self.current in self.id_chars: self.advance()
        return Token(Token.ExceedsLimit, self.get_lexeme(), self.start_line, self.start_col)
