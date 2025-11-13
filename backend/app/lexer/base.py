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

        # Character sets based on formal specification
        # underscore { _ }
        self.underscore = ['_']
        
        # zero { 0 }
        self.zero = ['0']
        
        # digit { 1, 2, 3, 4, 5, 6, 7, 8, 9 }
        self.digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        # numeric { <zero>, <digit> }
        self.numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        # lowercase { a, b, c, ..., z }
        self.lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        # uppercase { A, B, C, ..., Z }
        self.uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                          'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        # alpha { <lowercase>, <uppercase> }
        self.alpha = self.lowercase + self.uppercase
        
        # alphanumeric { <alpha>, <numeric> }
        self.alphanumeric = self.alpha + self.numeric
        
        # id_chars { <alphanumeric>, <underscore> }
        self.id_chars = self.alphanumeric + self.underscore
        
        # flag { up, down }
        self.flag = ['up', 'down']
        
        # arithm_op { +, -, *, /, % }
        self.arithm_op = ['+', '-', '*', '/', '%']
        
        # logic_op { and, or, not }
        self.logic_op = ['and', 'or', 'not']
        
        # assign_op { =, +=, -=, /=, *=, %= }
        self.assign_op = ['=', '+=', '-=', '/=', '*=', '%=']
        
        # rel_op { !=, ==, <, >, <=, >= }
        self.rel_op = ['!=', '==', '<', '>', '<=', '>=']
        
        # period { . }
        self.period = ['.']
        
        # newline { \n }
        self.newline = ['\n']
        
        # tab { \t }
        self.tab = ['\t']
        
        # space { ˽ }
        self.space = [' ']
        
        # whitespace { <newline>, <tab>, <space> }
        self.whitespace = ['\n', '\t', ' ']
        
        # ascii { <alphanumeric>, <arithm_op>, ˽, !, ", #, $, &, ', (, ), ,, ., :, ;, <, =, >, ?, @, [, \, ], ^, _, `, {, |, }, ~ }
        self.ascii = self.alphanumeric + self.arithm_op + [' ', '!', '"', '#', '$', '&', "'", '(', ')', ',', '.', ':', ';', '<', '=', '>', 
                                                            '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        
        # ascii_1 { <ascii excluding(\, ")> }
        self.ascii_1 = [c for c in self.ascii if c not in ['\\', '"']]
        
        # ascii_2 { <ascii>, \t }
        self.ascii_2 = self.ascii + ['\t']
        
        # ascii_3 { <ascii excluding(#)>, \n, \t }
        self.ascii_3 = [c for c in self.ascii if c != '#'] + ['\n', '\t']

        # Keywords
        self.KEYWORDS = [
            "alt", "and", "append", "bill", "chars", "check", "choice", "copy", "cut",
            "fact", "flag", "instead", "matches", "menu", "next", "not", "of", "or",
            "order", "pass", "piece", "pow", "prepare", "rand", "remove", "repeat",
            "reverse", "search", "serve", "sip", "size", "sort", "sqrt", "start",
            "stop", "table", "take", "tochars", "topiece", "tosip", "usual"
        ]

        # Delimiters based on formal specification
        # colon_dlm { <whitespace>, : }
        self.colon_dlm = self.whitespace + [':']
        
        # curly_dlm { <whitespace>, { }
        self.curly_dlm = self.whitespace + ['{']
        
        # dtype_dlm { <whitespace>, [ }
        self.dtype_dlm = self.whitespace + ['[']
        
        # equal_dlm { <whitespace>, <alphanum>, (, [, -, _, " }
        self.equal_dlm = self.whitespace + self.alphanumeric + ['(', '[', '-', '_', '"']
        
        # flag_dlm { <whitespace>, (, ), [, ], ;, =, !, " }
        self.flag_dlm = self.whitespace + ['(', ')', '[', ']', ';', '=', '!', '"']
        
        # id_delim { <whitespace>, (, ), [, ], ;, =, +, -, *, /, %, !, <, >, ,, : }
        self.id_delim = self.whitespace + ['(', ')', '[', ']', ';', '=', '+', '-', '*', '/', '%', '!', '<', '>', ',', ':', '#']
        
        # num_delim { <whitespace>, (, ), ], ;, =, +, -, *, /, %, !, <, >, ,, : }
        self.num_delim = self.whitespace + ['(', ')', ']', ';', '=', '+', '-', '*', '/', '%', '!', '<', '>', ',', ':']
        
        # op1_dlm { <whitespace>, <alphanum>, (, -, _, " }
        self.op1_dlm = self.whitespace + self.alphanumeric + ['(', '-', '_', '"']
        
        # op2_dlm { <whitespace>, <alpha>, (, _, " }
        self.op2_dlm = self.whitespace + self.alpha + ['(', '_', '"']
        
        # paren_dlm { <whitespace>, ( }
        self.paren_dlm = self.whitespace + ['(']
        
        # term_dlm { <whitespace>, ; }
        self.term_dlm = self.whitespace + [';']
        
        # Legacy delimiter (keeping for backward compatibility)
        self.whitespace_dlm = self.whitespace

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
        return self.current in delimiters

    def _error_invalid_char(self):
        """Handles an InvalidCharacter from s0."""
        self.advance()
        lexeme = self.text[self.pos-1:self.pos]
        return Token(Token.InvalidCharacter, lexeme, self.start_line, self.start_col + 1)
