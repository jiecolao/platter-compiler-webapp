from typing import Protocol, Optional, Tuple
from app.lexer.token import Token


class LexerProtocol(Protocol):

    # Position tracking
    text: str
    pos: int
    line: int
    col: int
    start_pos: int
    start_col: int
    start_line: int
    current: Optional[str]
    
    # Character sets
    ID_START: str
    ID_BODY: str
    DIGITS: str
    
    # Delimiters
    id_delim: str
    num_delim: str
    op1_dlm: str
    op2_dlm: str
    equal_dlm: str
    paren_dlm: str
    dtype_dlm: str
    curly_dlm: str
    term_dlm: str
    flag_dlm: str
    whitespace_dlm: str
    colon_dlm: str
    
    # Methods
    def advance(self) -> None: ...
    def save(self) -> Tuple[int, int, int, Optional[str]]: ...
    def restore(self, state: Tuple[int, int, int, Optional[str]]) -> None: ...
    def save_start(self) -> None: ...
    def get_lexeme(self) -> str: ...
    def _match_delimiter(self, delimiters: str) -> bool: ...
    def _error_invalid_char(self) -> Token: ...
