from app.lexer.lexer import Lexer
from app.parser.error_handler import ErrorHandler
from app.parser.predict_set_err import PREDICT_SET_ERR


class Parser():
    def __init__(self, tokens):
        self.tokens = [t for t in tokens if t.type not in ("space", "tab", "newline", "comment_single", "comment_multi")] # filter out ws and comments
        if not self.tokens: 
            raise ErrorHandler("EOF", None, PREDICT_SET_ERR["<program>"])
        
        self.pos = 0
    
    def parse_token(self, tok):
        """Parse and consume a specific token type"""
        if self.pos >= len(self.tokens):
            raise ErrorHandler("EOF", None, tok)    
        
        if self.tokens[self.pos].type == tok: 
            self.pos += 1
        else:
            raise ErrorHandler("Unexpected_err", self.tokens[self.pos], tok)

    def parse_program(self):
        """<program> -> <global_decl>* <recipe_decl>* start() <platter>"""
        # Parse global declarations
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in PREDICT_SET_ERR["<global_decl>"]:
            self.parse_global_decl()
        
        # Parse recipe declarations (prepare functions)
        while self.pos < len(self.tokens) and self.tokens[self.pos].type == "prepare":
            self.parse_recipe_decl()
        
        # Parse start() platter
        if self.pos >= len(self.tokens):
            raise ErrorHandler("EOF", None, "start")
        
        self.parse_token("start")
        self.parse_token("(")
        self.parse_token(")")
        self.parse_platter()
        
        # Ensure we've consumed all tokens
        if self.pos < len(self.tokens):
            raise ErrorHandler("ExpectedEOF_err", self.tokens[self.pos], None)
    
    def parse_global_decl(self):
        """<global_decl> -> <decl_data_type> of <ingredient_id> <ingredient_init> | table ..."""
        if self.tokens[self.pos].type in PREDICT_SET_ERR["<decl_data_type>"]:
            # piece, sip, flag, chars
            self.parse_token(self.tokens[self.pos].type)
            self.parse_token("of")
            self.parse_token("id")
            self.parse_ingredient_init()
        elif self.tokens[self.pos].type == "table":
            self.parse_table_prototype()
        elif self.tokens[self.pos].type == "id":
            # Custom type (table instance)
            self.parse_token("id")
            self.parse_token("of")
            self.parse_token("id")
            self.parse_ingredient_init()
        elif self.tokens[self.pos].type == "prepare":
            # This will be handled by recipe_decl
            return
        else:
            raise ErrorHandler("Unexpected_err", self.tokens[self.pos], PREDICT_SET_ERR["<global_decl>"])
    
    def parse_ingredient_init(self):
        """<ingredient_init> -> = <expr> <ingredient_id_tail> | <ingredient_id_tail>"""
        if self.pos < len(self.tokens) and self.tokens[self.pos].type == "=":
            self.parse_token("=")
            self.parse_expr()
        
        self.parse_ingredient_id_tail()
    
    def parse_ingredient_id_tail(self):
        """<ingredient_id_tail> -> , id <ingredient_init> | ;"""
        if self.pos < len(self.tokens) and self.tokens[self.pos].type == ",":
            self.parse_token(",")
            self.parse_token("id")
            self.parse_ingredient_init()
        else:
            self.parse_token(";")
    
    def parse_table_prototype(self):
        """table <id> { <required_decl>+ }"""
        self.parse_token("table")
        self.parse_token("id")
        self.parse_token("{")
        
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in PREDICT_SET_ERR["<required_decl>"]:
            self.parse_required_decl()
        
        self.parse_token("}")
        self.parse_token(";")
    
    def parse_required_decl(self):
        """<required_decl> -> <decl_data_type> of id ; | id of id ;"""
        if self.tokens[self.pos].type in PREDICT_SET_ERR["<decl_data_type>"]:
            self.parse_token(self.tokens[self.pos].type)
        else:
            self.parse_token("id")
        
        self.parse_token("of")
        self.parse_token("id")
        self.parse_token(";")
    
    def parse_recipe_decl(self):
        """prepare <serve_type> of id(<spice>) <platter>"""
        self.parse_token("prepare")
        
        # Parse return type (optional void)
        if self.pos < len(self.tokens) and self.tokens[self.pos].type in PREDICT_SET_ERR["<serve_type>"]:
            self.parse_token(self.tokens[self.pos].type)
            self.parse_token("of")
        
        self.parse_token("id")
        self.parse_token("(")
        self.parse_spice()
        self.parse_token(")")
        self.parse_platter()
    
    def parse_spice(self):
        """<spice> -> <serve_type> of id <spice_tail> | ε"""
        if self.pos < len(self.tokens) and self.tokens[self.pos].type in PREDICT_SET_ERR["<spice>"]:
            if self.tokens[self.pos].type != ")":
                self.parse_token(self.tokens[self.pos].type)
                self.parse_token("of")
                self.parse_token("id")
                self.parse_spice_tail()
    
    def parse_spice_tail(self):
        """<spice_tail> -> , <serve_type> of id <spice_tail> | ε"""
        if self.pos < len(self.tokens) and self.tokens[self.pos].type == ",":
            self.parse_token(",")
            self.parse_token(self.tokens[self.pos].type)
            self.parse_token("of")
            self.parse_token("id")
            self.parse_spice_tail()
    
    def parse_platter(self):
        """<platter> -> { <local_decl>* <statements>* }"""
        self.parse_token("{")
        
        # Parse local declarations and statements
        while self.pos < len(self.tokens) and self.tokens[self.pos].type != "}":
            if self.tokens[self.pos].type in PREDICT_SET_ERR["<decl_data_type>"] or \
               (self.tokens[self.pos].type == "id" and self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1].type == "of"):
                # Local declaration
                self.parse_local_decl()
            else:
                # Statement
                self.parse_statement()
        
        self.parse_token("}")
    
    def parse_local_decl(self):
        """Local variable declaration"""
        if self.tokens[self.pos].type in PREDICT_SET_ERR["<decl_data_type>"]:
            self.parse_token(self.tokens[self.pos].type)
        else:
            self.parse_token("id")
        
        self.parse_token("of")
        self.parse_token("id")
        self.parse_ingredient_init()
    
    def parse_statement(self):
        """Parse various statement types"""
        if self.pos >= len(self.tokens):
            return
        
        tok_type = self.tokens[self.pos].type
        
        if tok_type == "serve":
            self.parse_token("serve")
            if self.pos < len(self.tokens) and self.tokens[self.pos].type != ";":
                self.parse_expr()
            self.parse_token(";")
        elif tok_type == "check":
            self.parse_check_statement()
        elif tok_type == "id":
            self.parse_token("id")
            if self.pos < len(self.tokens) and self.tokens[self.pos].type in ["=", "+=", "-=", "*=", "/=", "%="]:
                self.parse_token(self.tokens[self.pos].type)
                self.parse_expr()
            self.parse_token(";")
        else:
            # Skip unknown statement for now
            self.pos += 1
    
    def parse_check_statement(self):
        """check(<expr>) <platter> instead <platter>"""
        self.parse_token("check")
        self.parse_token("(")
        self.parse_expr()
        self.parse_token(")")
        self.parse_platter()
        
        if self.pos < len(self.tokens) and self.tokens[self.pos].type == "instead":
            self.parse_token("instead")
            self.parse_platter()
    
    def parse_expr(self):
        """Simple expression parsing (placeholder)"""
        if self.pos >= len(self.tokens):
            raise ErrorHandler("EOF", None, "expression")
        
        # For now, just consume tokens that are part of expressions
        if self.tokens[self.pos].type in PREDICT_SET_ERR["<expr>"]:
            self.parse_token(self.tokens[self.pos].type)


if __name__ == "__main__":
    from app.utils.FileHandler import run_file
    
    filepath = "parser.platter"
    code = run_file(filepath)
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    try:
        parser.parse_program()
        print("Syntax OK")
    except SyntaxError as e:
        print(str(e))