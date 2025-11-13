from app.lexer.numericals import LexerNumericals
from app.lexer.token import Token
from app.lexer.base import LexerBase
from app.lexer.keywords import LexerKeywords
from app.lexer.operators import LexerOperators
from app.lexer.identifiers import LexerIdentifier
from app.lexer.char_com import LexerCharCom


class Lexer(LexerBase, LexerKeywords, LexerOperators, LexerIdentifier, LexerCharCom, LexerNumericals):
    def s0(self):
        if self.current is None: return None

        self.save_start()

        saved_state = self.save()
        tok = None

        if self.current == 'a': tok = self.s1()
        elif self.current == 'b': tok = self.s14()
        elif self.current == 'c': tok = self.s19()
        elif self.current == 'd': tok = self.s41()
        elif self.current == 'f': tok = self.s46()
        elif self.current == 'i': tok = self.s55()
        elif self.current == 'm': tok = self.s63()
        elif self.current == 'n': tok = self.s75()
        elif self.current == 'o': tok = self.s83()
        elif self.current == 'p': tok = self.s92()
        elif self.current == 'r': tok = self.s112()
        elif self.current == 's': tok = self.s134()
        elif self.current == 't': tok = self.s167()
        elif self.current == 'u': tok = self.s193()

        if tok: return tok
        self.restore(saved_state)

        if self.current == "+": return self.s201()
        if self.current == "-": return self.s205()
        if self.current == "*": return self.s209()
        if self.current == "/": return self.s213()
        if self.current == "%": return self.s217()
        if self.current == ">": return self.s221()
        if self.current == "<": return self.s225()
        if self.current == "=": return self.s229()
        if self.current == "!": return self.s233()

        if self.current == " ": return self.s236()
        if self.current == "\t": return self.s237()
        if self.current == "\n": return self.s238()
        if self.current == ":": return self.s239()
        if self.current == "{": return self.s240()
        if self.current == "}": return self.s241()
        if self.current == "(": return self.s242()
        if self.current == ")": return self.s243()
        if self.current == "[": return self.s244()
        if self.current == "]": return self.s245()
        if self.current == ",": return self.s246()
        if self.current == ";": return self.s247()

        if self.current in (self.alpha + self.underscore): return self.s248()
        if self.current == "0": return self.s298()
        if self.current in self.digit: return self.s300()
        if self.current == '"': return self.s345()
        if self.current == '#': return self.s348()

        return self._error_invalid_char()

    def tokenize(self):
        """Returns a list of all tokens from the input text."""
        tokens = []
        while self.current is not None:
            tok = self.s0()
            if not tok: break
            if isinstance(tok, list): tokens.extend(tok)
            else: tokens.append(tok)
        return tokens
