class Token:
    def __init__(self, type_, value, line, col):
        self.type = type_
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self):
        return f"{self.type:<30} | line={self.line:<3} | col={self.col:<3} | {self.value:<25}"


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

    def save(self):
        return (self.pos, self.col, self.current)

    def restore(self, s):
        self.pos, self.col, self.current = s

    # ----------------------------------------------------------
    def get_next_token(self):
        if self.current is None:
            return None

        start_pos = self.pos
        start_col = self.col

        # ---------- a ----------
        saved = self.save()
        if self.current == "a":
            self.advance()
            if self.current == "l":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("alt", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "n":
                self.advance()
                if self.current == "d":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("and", self.text[start_pos:self.pos], self.line, start_col)
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
                                if self.current is None or self.current in " \n\t(":
                                    return Token("append", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- b ----------
        saved = self.save()
        if self.current == "b":
            self.advance()
            if self.current == "i":
                self.advance()
                if self.current == "l":
                    self.advance()
                    if self.current == "l":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("bill", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- c ----------
        saved = self.save()
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
                            if self.current is None or self.current in " \n\t[":
                                return Token("chars", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "e":
                    self.advance()
                    if self.current == "c":
                        self.advance()
                        if self.current == "k":
                            self.advance()
                            if self.current is None or self.current in " \n\t(":
                                return Token("check", self.text[start_pos:self.pos], self.line, start_col)
                    elif self.current == "o":
                        self.advance()
                        if self.current == "i":
                            self.advance()
                            if self.current == "c":
                                self.advance()
                                if self.current == "e":
                                    self.advance()
                                    if self.current is None or self.current in " \n\t":
                                        return Token("choice", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "p":
                    self.advance()
                    if self.current == "y":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("copy", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "u":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("cut", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- d ----------
        saved = self.save()
        if self.current == "d":
            self.advance()
            if self.current == "o":
                self.advance()
                if self.current == "w":
                    self.advance()
                    if self.current == "n":
                        self.advance()
                        if self.current is None or self.current in " \n\t()[];=!\"":
                            return Token("flat_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)
        # ---------- f ----------
        saved = self.save()
        if self.current == "f":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "c":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("fact", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "l":
                self.advance()
                if self.current == "a":
                    self.advance()
                    if self.current == "g":
                        self.advance()
                        if self.current is None or self.current in " \n\t[":
                            return Token("flag", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- i ----------
        saved = self.save()
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
                                    if self.current is None or self.current in " \n\t{":
                                        return Token("instead", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- m ----------
        saved = self.save()
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
                                    if self.current is None or self.current in " \n\t(":
                                        return Token("matches", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "e":
                self.advance()
                if self.current == "n":
                    self.advance()
                    if self.current == "u":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("menu", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- n ----------
        saved = self.save()
        if self.current == "n":
            self.advance()
            if self.current == "e":
                self.advance()
                if self.current == "x":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t;":
                            return Token("next", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "t":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("not", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)
        # ---------- o ----------
        saved = self.save()
        if self.current == "o":
            self.advance()
            if self.current == "f":
                self.advance()
                if self.current is None or self.current in " \n\t":
                    return Token("of", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "r":
                self.advance()
                if self.current is None or self.current in " \n\t(":
                    return Token("or", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "d":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "r":
                            self.advance()
                            if self.current is None or self.current in " \n\t(":
                                return Token("order", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- p ----------
        saved = self.save()
        if self.current == "p":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "s":
                    self.advance()
                    if self.current == "s":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("pass", self.text[start_pos:self.pos], self.line, start_col)
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
                                    if self.current is None or self.current in " \n\t":
                                        return Token("prepare", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "i":
                self.advance()
                if self.current == "e":
                    self.advance()
                    if self.current == "c":
                        self.advance()
                        if self.current == "e":
                            self.advance()
                            if self.current is None or self.current in " \n\t[":
                                return Token("piece", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "w":
                    self.advance()
                    if self.current is None or self.current in " \n\t(":
                        return Token("pow", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- r ----------
        saved = self.save()
        if self.current == "r":
            self.advance()
            if self.current == "a":
                self.advance()
                if self.current == "n":
                    self.advance()
                    if self.current == "d":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("rand", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "e":
                self.advance()
                if self.current == "m":
                    self.advance()
                    if self.current == "o":
                        self.advance()
                        if self.current == "v":
                            self.advance()
                            if self.current == "e":
                                self.advance()
                                if self.current is None or self.current in " \n\t(":
                                    return Token("remove", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "p":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current == "a":
                            self.advance()
                            if self.current == "t":
                                self.advance()
                                if self.current is None or self.current in " \n\t(":
                                    return Token("repeat", self.text[start_pos:self.pos], self.line, start_col)
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
                                    if self.current is None or self.current in " \n\t(":
                                        return Token("reverse", self.text[start_pos:self.pos], self.line, start_col)
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
                                    if self.current is None or self.current in " \n\t(":
                                        return Token("search", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- s ----------
        saved = self.save()
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
                            if self.current is None or self.current in " \n\t":
                                return Token("serve", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "i":
                self.advance()
                if self.current == "p":
                    self.advance()
                    if self.current is None or self.current in " \n\t[":
                        return Token("sip", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "z":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("size", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "q":
                self.advance()
                if self.current == "r":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("sqrt", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "o":
                self.advance()
                if self.current == "r":
                    self.advance()
                    if self.current == "t":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("sort", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "t":
                self.advance()
                if self.current == "a":
                    self.advance()
                    if self.current == "r":
                        self.advance()
                        if self.current == "t":
                            self.advance()
                            if self.current is None or self.current in " \n\t(":
                                return Token("start", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "o":
                    self.advance()
                    if self.current == "p":
                        self.advance()
                        if self.current is None or self.current in " \n\t;":
                            return Token("stop", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- t ----------
        saved = self.save()
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
                            if self.current is None or self.current in " \n\t":
                                return Token("table", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "k":
                    self.advance()
                    if self.current == "e":
                        self.advance()
                        if self.current is None or self.current in " \n\t(":
                            return Token("take", self.text[start_pos:self.pos], self.line, start_col)
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
                                    if self.current is None or self.current in " \n\t(":
                                        return Token("tochars", self.text[start_pos:self.pos], self.line, start_col)
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
                                    if self.current is None or self.current in " \n\t(":
                                        return Token("topiece", self.text[start_pos:self.pos], self.line, start_col)
                elif self.current == "s":
                    self.advance()
                    if self.current == "i":
                        self.advance()
                        if self.current == "p":
                            self.advance()
                            if self.current is None or self.current in " \n\t(":
                                return Token("tosip", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # ---------- u ----------
        saved = self.save()
        if self.current == "u":
            self.advance()
            if self.current == "p":
                self.advance()
                if self.current is None or self.current in " \n\t()[];=!\"":
                    return Token("flag_lit", self.text[start_pos:self.pos], self.line, start_col)
            elif self.current == "s":
                self.advance()
                if self.current == "u":
                    self.advance()
                    if self.current == "a":
                        self.advance()
                        if self.current == "l":
                            self.advance()
                            if self.current is None or self.current in " \n\t:":
                                return Token("usual", self.text[start_pos:self.pos], self.line, start_col)
            self.restore(saved)

        # symbols

        op1_dlm = " \n\tabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789(-_“"
        op2_dlm = " \n\tabcdefghijklmnopqrstuvwxyz(_“"
        equal_dlm = " \n\tabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789([-_“"

        # +
        if self.current == "+":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("+=", "+=", self.line, self.col)
            if self.current is None or self.current in op1_dlm:
                return Token("+", "+", self.line, self.col)

        # -
        if self.current == "-":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("-=", "-=", self.line, self.col)
            if self.current is None or self.current in op2_dlm:
                return Token("-", "-", self.line, self.col)

        # *
        if self.current == "*":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("*=", "*=", self.line, self.col)
            if self.current is None or self.current in op1_dlm:
                return Token("*", "*", self.line, self.col)

        # /
        if self.current == "/":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("/=", "/=", self.line, self.col)
            if self.current is None or self.current in op1_dlm:
                return Token("/", "/", self.line, self.col)

        # %
        if self.current == "%":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("%=", "%=", self.line, self.col)
            if self.current is None or self.current in op1_dlm:
                return Token("%", "%", self.line, self.col)

        # >
        if self.current == ">":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token(">=", ">=", self.line, self.col)
            if self.current is None or self.current in op1_dlm:
                return Token(">", ">", self.line, self.col)

        # <
        if self.current == "<":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("<=", "<=", self.line, self.col)
            if self.current is None or self.current in op1_dlm:
                return Token("<", "<", self.line, self.col)

        # =
        if self.current == "=":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("==", "==", self.line, self.col)
            if self.current is None or self.current in equal_dlm:
                return Token("=", "=", self.line, self.col)

        # !
        if self.current == "!":
            self.advance()
            if self.current == "=":
                self.advance()
                if self.current is None or self.current in op1_dlm:
                    return Token("!=", "!=", self.line, self.col)
            return Token("!", "!", self.line, self.col)

        # space
        if self.current == " ":
            self.advance()
            return Token("space", "space", self.line, self.col)

        # tab
        if self.current == "\t":
            self.advance()
            return Token("tab", "tab", self.line, self.col)

        # newline
        if self.current == "\n":
            self.advance()
            return Token("newline", "newline", self.line, self.col)

        # colon
        if self.current == ":":
            self.advance()
            return Token(":", ":", self.line, self.col)

        # braces
        if self.current == "{":
            self.advance()
            return Token("{", "{", self.line, self.col)

        if self.current == "}":
            self.advance()
            return Token("}", "}", self.line, self.col)

        # parentheses
        if self.current == "(":
            self.advance()
            return Token("(", "(", self.line, self.col)

        if self.current == ")":
            self.advance()
            return Token(")", ")", self.line, self.col)

        # brackets
        if self.current == "[":
            self.advance()
            return Token("[", "[", self.line, self.col)

        if self.current == "]":
            self.advance()
            return Token("]", "]", self.line, self.col)

        # comma
        if self.current == ",":
            self.advance()
            return Token(",", ",", self.line, self.col)

        # semicolon
        if self.current == ";":
            self.advance()
            return Token(";", ";", self.line, self.col)

        # identifier
        id_delim = " \n\t()[];=+-*/%!<>,:"
        if self.current is not None and (self.current.isalpha() or self.current == "_"):
            start_col = self.col
            start_pos = self.pos

            if self.current is None or self.current in id_delim:
                return Token("id", "", self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            if self.current is None or self.current in id_delim:
                return Token("id", self.text[start_pos:self.pos], self.line, start_col)

        # numbers
        num_delim = " \n\t()[];=+-*/%!<>,:"
        if self.current is not None and (self.current.isdigit() or self.current == "-"):
            start_col = self.col
            start_pos = self.pos

            # negative
            if self.current == "-":
                self.advance()
                if self.current is None or self.current in num_delim:
                    return Token("-", "-", self.line, start_col)

            # digit 1
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 2
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif self.current.isdigit():
                goto_decimal = False
            else:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 3
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 4
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 5
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 6
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 7
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 8
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 9
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 10
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 11
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 12
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 13
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 14
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

            # digit 15 (last whole number digit)
            if self.current is None or self.current in num_delim:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            if self.current == ".":
                self.advance()
                goto_decimal = True
            elif not self.current.isdigit():
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)
            else:
                goto_decimal = False
            if not goto_decimal:
                return Token("piece_lit", self.text[start_pos:self.pos], self.line, start_col)

            # decimal part (7 digits max)
            # digit 1
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("sip_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            # digit 2
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("sip_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            # digit 3
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("sip_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            # digit 4
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("sip_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            # digit 5
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("sip_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            # digit 6
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("sip_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()
            # digit 7
            if self.current is None or self.current in num_delim or not self.current.isdigit():
                return Token("sip_lit", self.text[start_pos:self.pos], self.line, start_col)
            self.advance()

        # chars
        if self.current == '"':
            start_pos = self.pos
            start_col = self.col
            self.advance()
            while self.current is not None and self.current != '"':
                if self.current == "\\" and self.pos + 1 < len(self.text):
                    self.advance()
                self.advance()
            if self.current == '"':
                self.advance()
                return Token("chars_lit", self.text[start_pos:self.pos], self.line, start_col)
            return Token("UNKNOWN", self.text[start_pos:self.pos], self.line, start_col)

        # comments
        if self.current == "#":
            start_col = self.col
            self.advance()
            if self.current == "#":  # multi-line
                self.advance()
                start_pos = self.pos
                while self.current is not None:
                    if self.current == "#" and self.pos + 1 < len(self.text) and self.text[self.pos + 1] == "#":
                        self.advance()
                        self.advance()
                        return Token("comment_multi", self.text[start_pos:self.pos - 2], self.line, start_col)
                    self.advance()
                return Token("UNKNOWN", "#", self.line, start_col)
            elif self.current == " ":
                self.advance()
                start_pos = self.pos
                while self.current is not None and self.current != "\n":
                    self.advance()
                return Token("comment_single", self.text[start_pos:self.pos], self.line, start_col)
            return Token("UNKNOWN", "#", self.line, start_col)

        ch = self.current
        start_col = self.col
        self.advance()
        return Token("UNKNOWN", ch, self.line, start_col)

    def tokenize(self):
        tokens = []
        while True:
            tok = self.get_next_token()
            if tok is None:
                break
            tokens.append(tok)
        return tokens
