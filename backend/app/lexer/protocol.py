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
    ID_START: list[str]
    ID_BODY: list[str]
    NUMERIC: list[str]
    DIGIT: list[str]
    
    # Keywords
    KEYWORDS: list[str]
    
    # Delimiters
    id_delim: list[str]
    num_delim: list[str]
    op1_dlm: list[str]
    op2_dlm: list[str]
    equal_dlm: list[str]
    paren_dlm: list[str]
    dtype_dlm: list[str]
    curly_dlm: list[str]
    term_dlm: list[str]
    flag_dlm: list[str]
    whitespace_dlm: list[str]
    colon_dlm: list[str]
    
    # Methods
    def advance(self) -> None: ...
    def save(self) -> Tuple[int, int, int, Optional[str]]: ...
    def restore(self, state: Tuple[int, int, int, Optional[str]]) -> None: ...
    def save_start(self) -> None: ...
    def get_lexeme(self) -> str: ...
    def _match_delimiter(self, delimiters: list[str]) -> bool: ...
    def _error_invalid_char(self) -> Token: ...

    def s298(self) -> Token: ...
    def s301(self) -> Token: ...