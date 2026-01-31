class ErrorHandler:
  def __init__(self, error_type, tok, expected_toklist=None):
        if not tok:
                raise SyntaxError(f"Syntax Error: Program empty. Expected {expected_toklist}.")        
        errors = {
            "Unexpected_err": f"Syntax Error: Unexpected '{tok.current_tok}' at line {tok.current_line}, col {tok.current_col}. Expected {expected_toklist}.",
            "ExpectedEOF_err": f"Syntax Error: Unexpected token '{tok.current_tok}' after start platter, Expected EOF (line {tok.current_line}, col {tok.current_col})",
        }
        raise SyntaxError(errors[error_type])