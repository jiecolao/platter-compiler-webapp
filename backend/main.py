from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.lexer.lexer import Lexer
from app.parser.parser import Parser

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeInput(BaseModel):
    code: str

@app.get("/")
async def root():
    return {"message": "Platter Compiler Backend is running"}

@app.post("/analyzeLexical")
async def analyze_code(input_data: CodeInput):
    """Analyze Platter code and return lexemes"""
    try:
        lexer = Lexer(input_data.code)
        tokenize = lexer.tokenize()
        tokens = []
        
        for token in tokenize:
            if token is None:
                break
            tokens.append({
                "type": token.type,
                "value": token.value or '\\0',
                "line": token.line,
                "col": token.col
            })
        
        return {"tokens": tokens, "success": True}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Lexical analysis failed: {str(e)}")
    

@app.post("/analyzeSyntax")
async def analyze_syntax(input_data: CodeInput):
    """Analyze syntax of Platter code"""
    try:
        lexer = Lexer(input_data.code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        parser.parse()
        
        return {"message": "No Syntax Error", "success": True}
    except SyntaxError as e:
        return {"message": str(e), "success": False}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Syntax analysis failed: {str(e)}")