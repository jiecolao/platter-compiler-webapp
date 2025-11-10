from app.lexer.numericals import LexerNumericals
from app.lexer.token import Token
from app.lexer.base import LexerBase
from app.lexer.keywords import LexerKeywords
from app.lexer.operators import LexerOperators
from app.lexer.identifiers import LexerIdentifier
from app.lexer.char_com import LexerCharCom


class Lexer(LexerBase, LexerKeywords, LexerOperators, LexerIdentifier, LexerCharCom, LexerNumericals):
    """
    A Lexical Analyzer that tokenizes input character by character
    using a state machine based on the provided transition diagram.

    This class combines functionality from multiple mixins:
    - LexerBase: Core functionality and utilities
    - KeywordsMixin: Reserved word recognition
    - OperatorsMixin: Operator token recognition
    - IdentifiersMixin: Identifier token recognition
    - LiteralsMixin: Number, string, and comment recognition
    """

    def s0(self):
        """
        Initial state (dispatcher).
        Tries to match tokens in order of precedence:
        1. Reserved Words (must be tried first)
        2. Symbols
        3. Identifiers
        4. Literals (Numbers, Strings, Comments)
        5. Invalid Character
        """
        if self.current is None:
            return None

        self.save_start()

        saved_state = self.save()
        tok = None

        if self.current == 'a':
            tok = self.s1()
        elif self.current == 'b':
            tok = self.s14()
        elif self.current == 'c':
            tok = self.s19()
        elif self.current == 'd':
            tok = self.s41()
        elif self.current == 'f':
            tok = self.s46()
        elif self.current == 'i':
            tok = self.s55()
        elif self.current == 'm':
            tok = self.s63()
        elif self.current == 'n':
            tok = self.s75()
        elif self.current == 'o':
            tok = self.s83()
        elif self.current == 'p':
            tok = self.s92()
        elif self.current == 'r':
            tok = self.s112()
        elif self.current == 's':
            tok = self.s134()
        elif self.current == 't':
            tok = self.s167()
        elif self.current == 'u':
            tok = self.s193()

        if tok:
            return tok
        self.restore(saved_state)

        if self.current == "+": return self.s201()
        if self.current == "-":
            state_after_minus = self.save()
            self.advance()
            if self.current is not None and self.current in self.DIGITS:
                self.restore(state_after_minus)
                self.pos -= 1
                self.current = '-'
                return self.s_num_start()

            self.restore(saved_state)
            return self.s205()

        if self.current == "*": return self.s209()
        if self.current == "/": return self.s213()
        if self.current == "%": return self.s217()
        if self.current == ">": return self.s221()
        if self.current == "<": return self.s225()
        if self.current == "=": return self.s229()

        if self.current == "!":
            self.advance()
            if self.current == "=":
                self.advance()
                if self._match_delimiter(self.op1_dlm):
                    return Token("!=", "!=", self.start_line, self.start_col)
                return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)
            return Token(Token.InvalidLexeme, self.get_lexeme(), self.start_line, self.start_col)

        if self.current == " ": self.advance(); return Token("space", "space", self.start_line, self.start_col)
        if self.current == "\t": self.advance(); return Token("tab", "tab", self.start_line, self.start_col)
        if self.current == "\n": self.advance(); return Token("newline", "newline", self.start_line, self.start_col)
        if self.current == ":": self.advance(); return Token(":", ":", self.start_line, self.start_col)
        if self.current == "{": self.advance(); return Token("{", "{", self.start_line, self.start_col)
        if self.current == "}": self.advance(); return Token("}", "}", self.start_line, self.start_col)
        if self.current == "(": self.advance(); return Token("(", "(", self.start_line, self.start_col)
        if self.current == ")": self.advance(); return Token(")", ")", self.start_line, self.start_col)
        if self.current == "[": self.advance(); return Token("[", "[", self.start_line, self.start_col)
        if self.current == "]": self.advance(); return Token("]", "]", self.start_line, self.start_col)
        if self.current == ",": self.advance(); return Token(",", ",", self.start_line, self.start_col)
        if self.current == ";": self.advance(); return Token(";", ";", self.start_line, self.start_col)

        if self.current is not None and self.current in self.ID_START:
            return self.s248()

        if self.current is not None and self.current in self.DIGITS:
            return self.s_num_start()

        if self.current == '"':
            self.advance()
            return self.s345()

        if self.current == '#':
            self.advance()
            return self.s348()

        return self._error_invalid_char()

    def tokenize(self):
        """Returns a list of all tokens from the input text."""
        tokens = []
        while self.current is not None:
            tok = self.s0()
            if tok:
                if isinstance(tok, list):
                    tokens.extend(tok)
                else:
                    tokens.append(tok)
            else:
                break
        return tokens
