syntax_test = [
  {
    "number": 1,
    "name": "start() with no body",
    "code":  
    """
    start(){}
    """,
    "actual_output": "Syntax OK",
    "expected_output": "Syntax Error"
  },
  {
    "number": 2,
    "name": "prepare function with no complete header",
    "code":  
    """
    prepare(){}
    """,
    "actual_output": "Syntax OK",
    "expected_output": "Syntax Error"
  }
]