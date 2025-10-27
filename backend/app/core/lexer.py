class Token:
    def __init__(self, type_, value, line, col):
        self.type = type_
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self):
        return f"{self.type:<12} | line={self.line:<3} | col={self.col:<3} | {self.value:<10}"


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.col = 1
        self.current = self.text[self.pos] if self.text else None
    def advance(self):
        if self.current == "\n":
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        self.pos += 1
        self.current = self.text[self.pos] if self.pos < len(self.text) else None
    def get_next_token(self):
        while self.current is not None and self.current.isspace():
            self.advance()
        if self.current is None:
            return None
        start_col = self.col
        start_pos = self.pos
        if self.current == "a":
            self.advance()
            if self.current == "l":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                        return Token("ALT", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "n":
                self.advance()
                if self.current == "d":
                    self.advance()
                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                        return Token("AND", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "p":
                self.advance()
                if self.current == "p":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "n":
                            self.advance()
                            if self.current == "d":
                                self.advance()
                                if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                    return Token("APPEND", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "b":
            self.advance()
            if self.current == "i":
                self.advance()
                if self.current == "l":
                    self.advance()
                    if self.current == "l":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("BILL", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "c":
            self.advance()
            if self.current == "h":
                self.advance()
                if self.current == "a":
                    self.advance()
                    if self.current == "r":
                        self.advance()
                        if self.current == "s":
                            self.advance()
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("CHARS", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "e":
                    self.advance()
                    if self.current == "c":
                        self.advance()
                        if self.current == "k":
                            self.advance()
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("CHECK", self.text[start_pos:self.pos], self.line, start_col)
                    elif self.current == "o":
                        self.advance()
                        if self.current == "i":
                            self.advance()
                            if self.current == "c":
                                self.advance()
                                if self.current == "e":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("CHOICE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "p":
                    self.advance()
                    if self.current == "y":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("COPY", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "u":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                        return Token("CUT", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "d":
            self.advance()
            if self.current == "o":
                self.advance()
                if self.current == "w":
                    self.advance()
                    if self.current == "n":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("FLAG_LITERAL", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "f":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "c":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("FACT", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "l":
                self.advance()
                if self.current == "a":
                    self.advance()
                    if self.current == "g":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("FLAG", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "i":
            self.advance()
            if self.current == "n":
                self.advance()
                if self.current == "s":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current == "e":
                            self.advance()
                            if self.current == "a":
                                self.advance()
                                if self.current == "d":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("INSTEAD", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "m":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current == "c":
                        self.advance()
                        if self.current == "h":
                            self.advance()
                            if self.current == "e":
                                self.advance()
                                if self.current == "s":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("MATCHES", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "e":
                self.advance()
                if self.current == "n":
                    self.advance()
                    if self.current == "u":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("MENU", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "n":
            self.advance()
            if self.current == "e":
                self.advance()
                if self.current == "x":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("NEXT", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                        return Token("NOT", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "o":
            self.advance()
            if self.current == "f":
                self.advance()
                if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                    return Token("OF", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "r":
                self.advance()
                if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                    return Token("OR", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "r":
                self.advance()
                if self.current == "d":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "r":
                            self.advance()
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("ORDER", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "p":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "s":
                    self.advance()
                    if self.current == "s":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("PASS", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "r":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "p":
                            self.advance()
                            if self.current == "a":
                                self.advance()
                                if self.current == "r":
                                    self.advance()
                                    if self.current == "e":
                                        self.advance()
                                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                            return Token("PREPARE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "i":
                self.advance()
                if self.current == "e":
                    self.advance()
                    if self.current == "c":
                        self.advance()
                        if self.current == "e":
                            self.advance()
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("PIECE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "w":
                    self.advance()
                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                        return Token("POW", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "r":
            self.advance()
            if self.current == "e":
                self.advance()
                if self.current == "m":
                    self.advance()
                    if self.current == "o":
                        self.advance()
                        if self.current == "v":
                            self.advance()
                            if self.current == "e":
                                self.advance()
                                if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                    return Token("REMOVE", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "p":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "a":
                            self.advance()
                            if self.current == "t":
                                self.advance()
                                if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                    return Token("REPEAT", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "v":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "r":
                            self.advance()
                            if self.current == "s":
                                self.advance()
                                if self.current == "e":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("REVERSE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "s":
                self.advance()
                if self.current == "e":
                    self.advance()
                    if self.current == "a":
                        self.advance()
                        if self.current == "r":
                            self.advance()
                            if self.current == "c":
                                self.advance()
                                if self.current == "h":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("SEARCH", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "s":
            self.advance()
            if self.current == "e":
                self.advance()
                if self.current == "r":
                    self.advance()
                    if self.current == "v":
                        self.advance()
                        if self.current == "e":
                            self.advance()
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("SERVE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "i":
                self.advance()
                if self.current == "p":
                    self.advance()
                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                        return Token("SIP", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "z":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("SIZE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "q":
                self.advance()
                if self.current == "r":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("SQRT", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "r":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("SORT", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "t":
                self.advance()
                if self.current == "a":
                    self.advance()
                    if self.current == "r":
                        self.advance()
                        if self.current == "t":
                            self.advance()
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("START", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "t":
                self.advance()
                if self.current == "o":
                    self.advance()
                    if self.current == "p":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("STOP", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "t":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "b":
                    self.advance()
                    if self.current == "l":
                        self.advance()
                        if self.current == "e":
                            self.advance()
                            if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                return Token("TABLE", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "k":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                            return Token("TAKE", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "c":
                    self.advance()
                    if self.current == "h":
                        self.advance()
                        if self.current == "a":
                            self.advance()
                            if self.current == "r":
                                self.advance()
                                if self.current == "s":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("TOCHARS", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "p":
                    self.advance()
                    if self.current == "i":
                        self.advance()
                        if self.current == "e":
                            self.advance()
                            if self.current == "c":
                                self.advance()
                                if self.current == "e":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                                        return Token("TOPIECE", self.text[start_pos:self.pos], self.line, start_col)
        if self.current == "u":
            self.advance()
            if self.current == "p":
                self.advance()
                if self.current is None or self.current in " \n\t()[]{};=+-*/%!<>,:\"":
                    return Token("FLAG_LITERAL", self.text[start_pos:self.pos], self.line, start_col)
        if self.current in "{}()[];=+-*/%!<>,:\"\t\n ":
            ch = self.current
            self.advance()
            if ch in "+-*/%<>=!":
                if self.current == "=":
                    two = ch + "="
                    self.advance()
                    return Token(two, two, self.line, start_col)
            return Token(ch, ch, self.line, start_col)
        if self.current.isalpha() or self.current == "_":
            while self.current is not None and (self.current.isalnum() or self.current == "_"):
                self.advance()
            return Token("IDENTIFIER", self.text[start_pos:self.pos], self.line, start_col)
        # -------------------------------------------------------------------
        # string
        if self.current == '"':
            start_pos = self.pos
            self.advance()
            while self.current is not None and self.current != '"':
                if self.current == "\\" and self.pos + 1 < len(self.text):
                    self.advance()
                self.advance()
            if self.current == '"':
                self.advance()
                return Token("CHARS_LITERAL", self.text[start_pos + 1:self.pos - 1], self.line, start_col)

        # -------------------------------------------------------------------
        # number
        if self.current.isdigit():
            start_pos = self.pos
            has_dot = False
            while self.current is not None and (self.current.isdigit() or (self.current == "." and not has_dot)):
                if self.current == ".":
                    has_dot = True
                self.advance()
            return Token("SIP_LITERAL" if has_dot else "PIECE_LITERAL", self.text[start_pos:self.pos], self.line, start_col)

        # -------------------------------------------------------------------
        # comment
        if self.current == "#":
            self.advance()
            if self.current == "#":  # multi-line
                self.advance()
                start_pos = self.pos
                while self.current is not None:
                    if self.current == "#" and self.pos + 1 < len(self.text) and self.text[self.pos + 1] == "#":
                        self.advance()
                        self.advance()
                        return Token("COMMENT_MULTI", self.text[start_pos:self.pos - 2], self.line, start_col)
                    self.advance()
                return Token("UNKNOWN", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == " ":  # multi-line
                self.advance()
                start_pos = self.pos
                while self.current is not None and self.current != "\n":
                    self.advance()
                return Token("COMMENT_SINGLE", self.text[start_pos:self.pos], self.line, start_col)
        ch = self.current
        self.advance()
        return Token("UNKNOWN", ch, self.line, start_col)
    def tokenize(self):
        tokens = []
        while True:
            tok = self.get_next_token()
            tokens.append(tok)
            if tok is None:
                break
        return tokens
