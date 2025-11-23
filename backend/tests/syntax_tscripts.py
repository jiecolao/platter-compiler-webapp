SYNTAX_TSCRIPTS = [
  {
    "number": 1,
    "actual_output": "Syntax OK",
    "expected_output": "Syntax Error",
    "code":  
    """
    start(){} prepare
    """
  },
  {
    "number": 2,
    "actual_output": "Syntax OK",
    "expected_output": "Syntax Error",
    "code":  
    """
    prepare(){}
    """
  }
]