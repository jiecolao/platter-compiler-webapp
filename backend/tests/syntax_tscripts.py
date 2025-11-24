SYNTAX_TSCRIPTS = [
  { 
    "number": 3,
    "actual_output": "Syntax Error",
    "expected_output": "Syntax Error",
    "code":  
    """
    start(){
      prepare;){}
    }
    """
  },
  {
    "number": 4,
    "actual_output": "Syntax OK",
    "expected_output": "Syntax OK",
    "code":  
    """
    prepare(){}
    start(){}
    """
  },
  {
    "number": 5,
    "actual_output": "Syntax Error",
    "expected_output": "Syntax Error",
    "code":  
    """
    prepare (){}
    start(){} 
    """
  },
  {
    "number": 6,
    "actual_output": "Syntax Error",
    "expected_output": "Syntax Error",
    "code":  
    """
    check;;
    start(){}
    """
  },
  {
    "number": 7,
    "actual_output": "Syntax Error",
    "expected_output": "Syntax Error",
    "code":  
    """
    iwag of a = ;
    start(){
      
    }
    """
  }
]