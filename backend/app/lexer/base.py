from app.lexer.token import Token


class LexerBase:

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.col = 1
        self.start_pos = 0
        self.start_col = 1
        self.start_line = 1
        self.current = self.text[self.pos] if self.text else None

        self.ID_START = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']
        self.ID_BODY = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '0', '1', '2', '3',
                        '4', '5', '6', '7', '8', '9']
        self.DIGIT = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.NUMERIC = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Keywords
        self.KEYWORDS = [
            "alt", "and", "append", "bill", "chars", "check", "choice", "copy", "cut",
            "fact", "flag", "instead", "matches", "menu", "next", "not", "of", "or",
            "order", "pass", "piece", "pow", "prepare", "rand", "remove", "repeat",
            "reverse", "search", "serve", "sip", "size", "sort", "sqrt", "start",
            "stop", "table", "take", "tochars", "topiece", "tosip", "usual"
        ]

        self.id_delim = [' ', '\t', '\n', '(', ')', '[', ']', ';', '=', '+', '-', '*', '/', '%', '!', '<', '>', ',',
                         ':', '#']
        self.num_delim = [' ', '\t', '\n', '(', ')', '[', ']', ',', ';', '=', '+', '-', '*', '/', '%', '!', '<', '>',
                          ',', ':']

        self.op1_dlm = [' ', '\t', '\n', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '0',
                        '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', '_', '"']
        self.op2_dlm = [' ', '\t', '\n', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '(', '_', '"']
        self.equal_dlm = [' ', '\t', '\n', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                          'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                          'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_',
                          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', '[', '_', '"']

        self.paren_dlm = [' ', '\n', '\t', '(']
        self.dtype_dlm = [' ', '\n', '\t', '[']
        self.curly_dlm = [' ', '\n', '\t', '{']
        self.term_dlm = [' ', '\n', '\t', ';']
        self.flag_dlm = [' ', '\n', '\t', '(', ')', '[', ']', ';', '=', '!', '"']
        self.whitespace_dlm = [' ', '\n', '\t']
        self.colon_dlm = [' ', '\n', '\t', ':']

    def advance(self):
        """Moves to the next character, updating line and column."""
        if self.current == "\n":
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        self.pos += 1
        self.current = self.text[self.pos] if self.pos < len(self.text) else None

    def save(self):
        """Saves the current position, line, and column for backtracking."""
        return (self.pos, self.line, self.col, self.current)

    def restore(self, state):
        """Restores a saved state."""
        self.pos, self.line, self.col, self.current = state

    def save_start(self):
        """Saves the starting position for the current potential token."""
        self.start_pos = self.pos
        self.start_col = self.col
        self.start_line = self.line

    def get_lexeme(self):
        """Returns the lexeme value from the start position to the current position."""
        return self.text[self.start_pos:self.pos]

    def _match_delimiter(self, delimiters):
        """Checks if the current character is a valid delimiter for an accepting state."""
        return self.current is None or self.current in delimiters

    def _error_invalid_char(self):
        """Handles an InvalidCharacter from s0."""
        self.advance()
        lexeme = self.text[self.pos-1:self.pos]
        return Token(Token.InvalidCharacter, lexeme, self.start_line, self.start_col)
