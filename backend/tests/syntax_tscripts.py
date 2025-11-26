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
  },
  {
    "number": 8,
    "actual_output": "Syntax Error",
    "expected_output": "Syntax Error",
    "code":  
    """
    piece of a; 
    sip of b = ((3+5*2) and ) 5>10);
    table of a = [
      piece of x;
    ];

    start(){
    }
      
    }
    """
  },
  {
    "number": 9,
    "actual_output": "Syntax Error",
    "expected_output": "Syntax Error",
    "code":  
    """
    piece of a = piece # Must also consider invalid error
    start(){}
    """
  },
  {
    "number": 10,
    "actual_output": "Syntax Error",
    "expected_output": "Syntax Error",
    "code":  
    """
    a of a = :
    start(){}
    """
  },
]