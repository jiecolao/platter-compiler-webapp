class ErrorHandler:
  def __init__(self, error_type, tok, expected_toklist=None):
        # Format expected_toklist nicely if it's a list
        if isinstance(expected_toklist, list):
            formatted_expected = ", ".join(f"'{tok}'" for tok in expected_toklist)
        else:
            formatted_expected = expected_toklist
        
        if not tok:
                raise SyntaxError(f"Syntax Error: Unexpected EOF. Expected {formatted_expected}.")        
        errors = {
            "EOF":f"Syntax Error: Unexpected EOF. Expected {formatted_expected}.",
            "Unexpected_err": f"Syntax Error: Unexpected '{tok.type}' at line {tok.line}, col {tok.col}. Expected {formatted_expected}.",
            "ExpectedEOF_err": f"Syntax Error: Unexpected token '{tok.type}' after start platter, Expected EOF (line {tok.line}, col {tok.col})",
        }
        raise SyntaxError(errors[error_type])