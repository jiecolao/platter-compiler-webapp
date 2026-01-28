from app.lexer.lexer import Lexer
from app.parser.predict_set import PREDICT_SET
from app.parser.predict_set_err import PREDICT_SET_ERR
from tests.test_parser_util import run_file
import logging as log                           

from app.parser.ast_nodes import *

# To disable logs, set level=log.CRITICAL. 
# To enable logs, set level=log.DEBUG
log.basicConfig(level=log.CRITICAL, format='%(levelname)s: <%(funcName)s> | %(message)s')

class Parser:

    def __init__(self, tokens):
        """ Token Stream """
        self.tokenlist = [t for t in tokens if t.type not in ("space", "tab", "newline", "comment_single", "comment_multi")] # filter out ws and comments
        self.result = True
        self.ast_root = None  # Will hold the AST after parse_semantic

        """ Properties """
        self.tokens = [t.type for t in self.tokenlist]
        self.tokens_length = len(self.tokens)-1
        self.pos = 0

        """ Token Attributes """
        if self.tokens: # catch for empty tokens
            self.current_tok = self.tokens[self.pos] 
            self.current_line = self.tokenlist[self.pos].line 
            self.current_col = (self.tokenlist[self.pos].col) 
        else:
            self.current_tok = None
            self.current_line = None
            self.current_col = None


    def parse_token(self, tok):
        if self.current_tok == tok: 
            log.warning(f"Expected: {tok} | Current: {self.current_tok} | Remark: MATCH!")
            # print(f"├──Expected: {tok} | Current: {self.current_tok} | Remark: MATCH!")
            self.advance(tok)
        else:
            log.warning(f"Expected: {tok} | Current: {self.current_tok} | Remark: INVALID!\n")
            # print(f"└──Expected: {tok} | Current: {self.current_tok} | Remark: INVALID!")
            self.result = False
            self.error_handler("Unexpected_err", tok)

    def advance(self, tok): 
        if self.pos < self.tokens_length:
            self.pos += 1
            self.upd_tok_attr()
            log.warning(f"Consuming: {tok} -> {self.current_tok}\n")
            # print(f"└──Consuming: {tok} -> {self.current_tok}")
        else: 
            self.current_tok = "EOF" # end of token list, EOF reached
            # print(f"└──Consuming: {tok} -> {self.current_tok}")
            log.warning(f"Consuming: {tok} -> EOF\n")
            # raise SyntaxError (f"Syntax Error: Expected '{tok}' but got {self.current_tok}")

    def upd_tok_attr(self):
        self.current_tok = self.tokens[self.pos] 
        self.current_line = self.tokenlist[self.pos].line
        self.current_col = self.tokenlist[self.pos].col
    
    def get_current_token_value(self):
        """Get the actual value of the current token"""
        return self.tokenlist[self.pos].value if self.pos < len(self.tokenlist) else None

    def error_handler(self, error_type, tok, expected_toklist=None):        
        errors = {
            "Parse_err": f"Syntax Error: Program empty. Expected {tok}.",
            "Unexpected_err": f"Syntax Error: Unexpected '{self.current_tok}' at line {self.current_line}, col {self.current_col}. Expected {tok}.",
            
            "Program_err": f"Syntax Error: Program cannot begin with token '{self.current_tok}'. Expected a declaration or 'prepare/start'",
            "ExpectedEOF_err": f"Syntax Error: Unexpected token '{self.current_tok}' after start platter, Expected EOF (line {self.current_line}, col {self.current_col})",
            "Invalid_err": f"Syntax Error: Invalid {tok} at line {self.current_line}, col {self.current_col}.",
            "Invalid_err1": f"Syntax Error: Invalid {tok} at line {self.current_line}, col {self.current_col}. Expected {expected_toklist}",
            "Missing_err": f"Syntax Error: Missing {tok} at line {self.current_line}, col {self.current_col}",
            "Custom_err": f"Syntax Error: {tok} (line {self.current_line}, col {self.current_col})",
        }
        self.result = False
        raise SyntaxError(errors[error_type])

    # CFG Parsing Methods 

    def parse(self):
        if self.tokenlist:
            self.ast_root = self.program()
        else: self.error_handler("Parse_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<program>"])))
        return self.ast_root
    
    def program(self):
        program_node = Program()
        log.info("Enter: " + self.current_tok)

        if self.current_tok in PREDICT_SET_ERR["<program>"]:
            if self.current_tok in PREDICT_SET["<program>"]:
                self.global_decl(program_node) 
            if self.current_tok in PREDICT_SET["<recipe_decl>"]:
                self.recipe_decl(program_node) 
            self.parse_token("start")
            self.parse_token("(")
            self.parse_token(")")
            start_platter_node = self.platter()
            program_node.set_start_platter(start_platter_node)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<program>"])))

        # Ensure EOF after parsing
        if self.current_tok != "EOF": self.error_handler("ExpectedEOF_err", None) 
        log.info("Exit: " + self.current_tok)
        
        return program_node

    def global_decl(self, program_node):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<global_decl>"]:
            if self.current_tok in PREDICT_SET["<global_decl>"]: # if has null in set
                decl_node = self.decl_data_type()
                if decl_node:
                    program_node.add_global_decl(decl_node)
                self.global_decl(program_node)
            if self.current_tok in PREDICT_SET["<global_decl_1>"]:
                table_proto_node = self.table_prototype()
                if table_proto_node:
                    program_node.add_global_decl(table_proto_node)
                self.global_decl(program_node) 
            if self.current_tok in PREDICT_SET["<global_decl_2>"]:
                table_name = self.get_current_token_value()
                self.parse_token("id")
                table_decl_node = self.table_decl(table_name)
                if table_decl_node:
                    program_node.add_global_decl(table_decl_node)
                self.global_decl(program_node)
            if self.current_tok in PREDICT_SET["<global_decl_3>"]:
                log.info("Exit: " + self.current_tok)
                return # λ
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<global_decl>"])))
        log.info("Exit: " + self.current_tok)

    def decl_data_type(self):
        log.info("Enter: " + self.current_tok)
        data_type = None
        if self.current_tok in PREDICT_SET_ERR["<decl_data_type>"]: # if no null in set
            if self.current_tok in PREDICT_SET["<decl_data_type>"]:
                data_type = "piece"
                self.parse_token("piece")
                return self.decl_type(data_type)
            if self.current_tok in PREDICT_SET["<decl_data_type_1>"]:
                data_type = "sip"
                self.parse_token("sip")
                return self.decl_type(data_type)
            if self.current_tok in PREDICT_SET["<decl_data_type_2>"]:
                data_type = "flag"
                self.parse_token("flag")
                return self.decl_type(data_type)
            if self.current_tok in PREDICT_SET["<decl_data_type_3>"]:
                data_type = "chars"
                self.parse_token("chars")
                return self.decl_type(data_type)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<decl_data_type>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def decl_type(self, data_type):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<decl_type>"]:
            if self.current_tok in PREDICT_SET["<decl_type>"]:
                self.parse_token("of")
                id_and_inits = self.ingredient_id()
                self.parse_token(";")
                return IngredientDecl(data_type, 0, id_and_inits)
            if self.current_tok in PREDICT_SET["<decl_type_1>"]:
                dims = self.dimensions()
                self.parse_token("of")
                id_and_inits = self.array_declare()
                self.parse_token(";")
                return IngredientDecl(data_type, dims, id_and_inits)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<decl_type>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def ingredient_id(self):
        log.info("Enter: " + self.current_tok)
        id_and_inits = []
        if self.current_tok in PREDICT_SET_ERR["<ingredient_id>"]:
            if self.current_tok in PREDICT_SET["<ingredient_id>"]:
                identifier = self.get_current_token_value()
                self.parse_token("id")
                init_value = self.ingredient_init()
                id_and_inits.append(IdAndInit(identifier, init_value))
                more_ids = self.ingredient_id_tail()
                id_and_inits.extend(more_ids)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<ingredient_id>"])))
        log.info("Exit: " + self.current_tok)
        return id_and_inits
        
    def ingredient_init(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<ingredient_init>"]:
            if self.current_tok in PREDICT_SET["<ingredient_init>"]:
                self.parse_token("=")
                return self.expr()
            if self.current_tok in PREDICT_SET["<ingredient_init_1>"]:
                log.info("Exit: " + self.current_tok)
                return None # λ - no initialization
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<ingredient_init>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def ingredient_id_tail(self):
        log.info("Enter: " + self.current_tok)
        id_and_inits = []
        if self.current_tok in PREDICT_SET_ERR["<ingredient_id_tail>"]:
            if self.current_tok in PREDICT_SET["<ingredient_id_tail>"]:
                self.parse_token(",")
                identifier = self.get_current_token_value()
                self.parse_token("id")
                init_value = self.ingredient_init()
                id_and_inits.append(IdAndInit(identifier, init_value))
                more_ids = self.ingredient_id_tail()
                id_and_inits.extend(more_ids)
            if self.current_tok in PREDICT_SET["<ingredient_id_tail_1>"]:
                log.info("Exit: " + self.current_tok)
                return [] # λ - no more identifiers
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<ingredient_id_tail>"])))
        log.info("Exit: " + self.current_tok)
        return id_and_inits
    
    def expr(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<expr>"]:
            if self.current_tok in PREDICT_SET["<expr>"]:
                return self.or_expr()
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<expr>"])))
        log.info("Exit: " + self.current_tok)
        return None
    
    def or_expr(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<or_expr>"]:
            if self.current_tok in PREDICT_SET["<or_expr>"]:
                left = self.and_expr()
                return self.or_tail(left)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<or_expr>"])))
        log.info("Exit: " + self.current_tok)
        return None
    
    def and_expr(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<and_expr>"]:
            if self.current_tok in PREDICT_SET["<and_expr>"]:
                left = self.eq_expr()
                return self.and_tail(left) 
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<and_expr>"])))
        log.info("Exit: " + self.current_tok)
        return None
    
    def or_tail(self, left):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET["<or_tail>"]:
            self.parse_token("or")
            right = self.and_expr()
            new_left = BinaryOp("or", left, right)
            return self.or_tail(new_left)
        if self.current_tok in PREDICT_SET["<or_tail_1>"]:
            log.info("Exit: " + self.current_tok)
            return left
        log.info("Exit: " + self.current_tok)
        return left
        
    def eq_expr(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<eq_expr>"]:
            if self.current_tok in PREDICT_SET["<eq_expr>"]:
                left = self.rel_expr()
                return self.eq_tail(left)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<eq_expr>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def and_tail(self, left):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET["<and_tail>"]:
            self.parse_token("and")
            right = self.eq_expr()
            new_left = BinaryOp("and", left, right)
            return self.and_tail(new_left)
        if self.current_tok in PREDICT_SET["<and_tail_1>"]:
            log.info("Exit: " + self.current_tok)
            return left
        log.info("Exit: " + self.current_tok)
        return left
    
    def rel_expr(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<rel_expr>"]:
            if self.current_tok in PREDICT_SET["<rel_expr>"]:
                left = self.add_expr()
                return self.rel_tail(left)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<rel_expr>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def eq_tail(self, left):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET["<eq_tail>"]:
            self.parse_token("==")
            right = self.rel_expr()
            new_left = BinaryOp("==", left, right)
            return self.eq_tail(new_left)
        if self.current_tok in PREDICT_SET["<eq_tail_1>"]:
            self.parse_token("!=")
            right = self.rel_expr()
            new_left = BinaryOp("!=", left, right)
            return self.eq_tail(new_left)
        if self.current_tok in PREDICT_SET["<eq_tail_2>"]:
            log.info("Exit: " + self.current_tok)
            return left
        log.info("Exit: " + self.current_tok)
        return left

    def add_expr(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<add_expr>"]:
            if self.current_tok in PREDICT_SET["<add_expr>"]:
                left = self.mult_expr()
                return self.add_tail(left)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<add_expr>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def rel_expr(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<rel_expr>"]:
            if self.current_tok in PREDICT_SET["<rel_expr>"]:
                left = self.add_expr()
                return self.rel_tail(left)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<rel_expr>"])))
        log.info("Exit: " + self.current_tok)
        return None
            
    def rel_tail(self, left):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET["<rel_tail>"]:
            self.parse_token(">")
            right = self.add_expr()
            new_left = BinaryOp(">", left, right)
            return self.rel_tail(new_left)
        if self.current_tok in PREDICT_SET["<rel_tail_1>"]:
            self.parse_token("<")
            right = self.add_expr()
            new_left = BinaryOp("<", left, right)
            return self.rel_tail(new_left)
        if self.current_tok in PREDICT_SET["<rel_tail_2>"]:
            self.parse_token(">=")
            right = self.add_expr()
            new_left = BinaryOp(">=", left, right)
            return self.rel_tail(new_left)
        if self.current_tok in PREDICT_SET["<rel_tail_3>"]:
            self.parse_token("<=")
            right = self.add_expr()
            new_left = BinaryOp("<=", left, right)
            return self.rel_tail(new_left)
        if self.current_tok in PREDICT_SET["<rel_tail_4>"]:
            log.info("Exit: " + self.current_tok)
            return left
        log.info("Exit: " + self.current_tok)
        return left
        
    def mult_expr(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<mult_expr>"]:
            if self.current_tok in PREDICT_SET["<mult_expr>"]:
                left = self.unary_expr()
                return self.mult_tail(left)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<mult_expr>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def add_tail(self, left):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET["<add_tail>"]:
            self.parse_token("+")
            right = self.mult_expr()
            new_left = BinaryOp("+", left, right)
            return self.add_tail(new_left)
        if self.current_tok in PREDICT_SET["<add_tail_1>"]:
            self.parse_token("-")
            right = self.mult_expr()
            new_left = BinaryOp("-", left, right)
            return self.add_tail(new_left)
        if self.current_tok in PREDICT_SET["<add_tail_2>"]:
            log.info("Exit: " + self.current_tok)
            return left
        log.info("Exit: " + self.current_tok)
        return left

    def unary_expr(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<unary_expr>"]:
            if self.current_tok in PREDICT_SET["<unary_expr>"]:
                self.parse_token("not")
                operand = self.unary_expr()
                return UnaryOp("!", operand)
            if self.current_tok in PREDICT_SET["<unary_expr_1>"]:
                return self.primary_val()
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<unary_expr>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def mult_tail(self, left):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET["<mult_tail>"]:
            self.parse_token("*")
            right = self.unary_expr()
            new_left = BinaryOp("*", left, right)
            return self.mult_tail(new_left)
        if self.current_tok in PREDICT_SET["<mult_tail_1>"]:
            self.parse_token("/")
            right = self.unary_expr()
            new_left = BinaryOp("/", left, right)
            return self.mult_tail(new_left)
        if self.current_tok in PREDICT_SET["<mult_tail_2>"]:
            self.parse_token("%")
            right = self.unary_expr()
            new_left = BinaryOp("%", left, right)
            return self.mult_tail(new_left)
        if self.current_tok in PREDICT_SET["<mult_tail_3>"]:
            log.info("Exit: " + self.current_tok)
            return left
        log.info("Exit: " + self.current_tok)
        return left

    def primary_val(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<primary_val>"]:
            if self.current_tok in PREDICT_SET["<primary_val>"]:
                self.parse_token("(")
                expr_node = self.expr()
                self.parse_token(")")
                return expr_node
            if self.current_tok in PREDICT_SET["<primary_val_1>"]:
                value = self.get_current_token_value()
                self.parse_token("piece_lit")
                return Literal("piece_lit", value)
            if self.current_tok in PREDICT_SET["<primary_val_2>"]:
                value = self.get_current_token_value()
                self.parse_token("sip_lit")
                return Literal("sip_lit", value)
            if self.current_tok in PREDICT_SET["<primary_val_3>"]:
                value = self.get_current_token_value()
                self.parse_token("flag_lit")
                return Literal("flag_lit", value)
            if self.current_tok in PREDICT_SET["<primary_val_4>"]:
                value = self.get_current_token_value()
                self.parse_token("chars_lit")
                return Literal("chars_lit", value)
            if self.current_tok in PREDICT_SET["<primary_val_5>"]:
                identifier = self.get_current_token_value()
                self.parse_token("id")
                return self.id_tail(identifier)
            if self.current_tok in PREDICT_SET["<primary_val_6>"]:
                return self.built_in_rec_call()
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<primary_val>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def id_tail(self, identifier):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<id_tail>"]:
            if self.current_tok in PREDICT_SET["<id_tail>"]:
                arguments = self.call_tailopt()
                indices = self.accessor_tail()
                if arguments is not None:
                    # It's a function call
                    return RecipeCall(identifier, arguments, indices)
                else:
                    # It's a variable reference
                    return Identifier(identifier, indices)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<id_tail>"])))
        log.info("Exit: " + self.current_tok)
        return Identifier(identifier, [])
        
    def call_tailopt(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<call_tailopt>"]:
            if self.current_tok in PREDICT_SET["<call_tailopt>"]:
                self.parse_token("(")
                arguments = self.flavor()
                self.parse_token(")")
                return arguments
            if self.current_tok in PREDICT_SET["<call_tailopt_1>"]:
                log.info("Exit: " + self.current_tok)
                return None # No function call
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<call_tailopt>"])))
        log.info("Exit: " + self.current_tok)
        return None
        
    def accessor_tail(self):
        log.info("Enter: " + self.current_tok)
        indices = []
        if self.current_tok in PREDICT_SET_ERR["<accessor_tail>"]:
            if self.current_tok in PREDICT_SET["<accessor_tail>"]:
                indices = self.array_accessor()
            if self.current_tok in PREDICT_SET["<accessor_tail_1>"]:
                indices = self.table_accessor()
            if self.current_tok in PREDICT_SET["<accessor_tail_2>"]:
                log.info("Exit: " + self.current_tok)
                return []
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<accessor_tail>"])))
        log.info("Exit: " + self.current_tok)
        return indices
        
    def array_accessor(self):
        log.info("Enter: " + self.current_tok)
        indices = []
        if self.current_tok in PREDICT_SET_ERR["<array_accessor>"]:
            if self.current_tok in PREDICT_SET["<array_accessor>"]:
                self.parse_token("[")
                index_expr = self.expr()
                indices.append(index_expr)
                self.parse_token("]")
                more_indices = self.accessor_tail()
                indices.extend(more_indices)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<array_accessor>"])))
        log.info("Exit: " + self.current_tok)
        return indices

    def table_accessor(self):
        log.info("Enter: " + self.current_tok)
        indices = []
        if self.current_tok in PREDICT_SET_ERR["<table_accessor>"]:
            if self.current_tok in PREDICT_SET["<table_accessor>"]:
                self.parse_token(":")
                field_name = self.get_current_token_value()
                self.parse_token("id")
                # Table access uses identifier as string literal index
                indices.append(Literal("field_name", field_name))
                more_indices = self.accessor_tail()
                indices.extend(more_indices)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<table_accessor>"])))
        log.info("Exit: " + self.current_tok)
        return indices

    def flavor(self):
        log.info("Enter: " + self.current_tok)
        arguments = []
        if self.current_tok in PREDICT_SET_ERR["<flavor>"]:
            if self.current_tok in PREDICT_SET["<flavor>"]:
                first_arg = self.value()
                arguments.append(first_arg)
                more_args = self.flavor_tail()
                arguments.extend(more_args)
            elif self.current_tok in PREDICT_SET["<flavor_1>"]:
                log.info("Exit: " + self.current_tok)
                return []
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<flavor>"])))
        log.info("Exit: " + self.current_tok)
        return arguments

    def value(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<value>"]:
            if self.current_tok in PREDICT_SET["<value>"]:
                return self.expr()
            if self.current_tok in PREDICT_SET["<value_1>"]:
                self.parse_token("[")
                array_or_table_node = self.notation_val()
                self.parse_token("]")
                indices = self.accessor_tail()
                # Add indices to the array/table literal if any
                if indices and isinstance(array_or_table_node, (ArrayLiteral, TableLiteral)):
                    # Wrap in identifier-like access (not standard but handles edge case)
                    pass
                return array_or_table_node
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<value>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def notation_val(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<notation_val>"]:
            if self.current_tok in PREDICT_SET["<notation_val>"]:
                # Array literal
                return self.array_element()
            if self.current_tok in PREDICT_SET["<notation_val_1>"]:
                # Table literal or array with id
                first_id = self.get_current_token_value()
                self.parse_token("id")
                return self.array_or_table(first_id)
            if self.current_tok in PREDICT_SET["<notation_val_2>"]:
                log.info("Exit: " + self.current_tok)
                return ArrayLiteral([])  # Empty array
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<notation_val>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def array_element(self):
        log.info("Enter: " + self.current_tok)
        array_node = ArrayLiteral()
        if self.current_tok in PREDICT_SET_ERR["<array_element>"]:
            if self.current_tok in PREDICT_SET["<array_element>"]:
                value = self.get_current_token_value()
                self.parse_token("piece_lit")
                array_node.add_element(Literal("piece_lit", value))
                self.element_value_tail(array_node)
            if self.current_tok in PREDICT_SET["<array_element_1>"]:
                value = self.get_current_token_value()
                self.parse_token("sip_lit")
                array_node.add_element(Literal("sip_lit", value))
                self.element_value_tail(array_node)
            if self.current_tok in PREDICT_SET["<array_element_2>"]:
                value = self.get_current_token_value()
                self.parse_token("flag_lit")
                array_node.add_element(Literal("flag_lit", value))
                self.element_value_tail(array_node)
            if self.current_tok in PREDICT_SET["<array_element_3>"]:
                value = self.get_current_token_value()
                self.parse_token("chars_lit")
                array_node.add_element(Literal("chars_lit", value))
                self.element_value_tail(array_node)
            if self.current_tok in PREDICT_SET["<array_element_4>"]:
                log.info("Exit: " + self.current_tok)
                return array_node
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<array_element>"])))
        log.info("Exit: " + self.current_tok)
        return array_node

    def element_value_tail(self, array_node):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<element_value_tail>"]:
            if self.current_tok in PREDICT_SET["<element_value_tail>"]:
                self.parse_token(",")
                self.array_element_id(array_node)
            if self.current_tok in PREDICT_SET["<element_value_tail_1>"]:
                log.info("Exit: " + self.current_tok)
                return
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<element_value_tail>"])))
        log.info("Exit: " + self.current_tok)

    def array_element_id(self, array_node):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<array_element_id>"]:
            if self.current_tok in PREDICT_SET["<array_element_id>"]:
                identifier = self.get_current_token_value()
                self.parse_token("id")
                array_node.add_element(Identifier(identifier, []))
                self.element_value_tail(array_node)
            if self.current_tok in PREDICT_SET["<array_element_id_1>"]:
                nested_array = self.array_element()
                array_node.add_element(nested_array)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<array_element_id>"])))
        log.info("Exit: " + self.current_tok)

    def array_or_table(self, first_id):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<array_or_table>"]:
            if self.current_tok in PREDICT_SET["<array_or_table>"]:
                # Array with identifier elements
                array_node = ArrayLiteral()
                array_node.add_element(Identifier(first_id, []))
                self.parse_token(",")
                self.array_element_id(array_node)
                return array_node
            if self.current_tok in PREDICT_SET["<array_or_table_1>"]:
                # Table literal
                table_node = TableLiteral()
                self.parse_token("=")
                value = self.value()
                table_node.add_field(first_id, value)
                self.parse_token(";")
                self.field_assignments(table_node)
                return table_node
            if self.current_tok in PREDICT_SET["<array_or_table_2>"]:
                # Single element array
                array_node = ArrayLiteral()
                array_node.add_element(Identifier(first_id, []))
                return array_node
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<array_or_table>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def field_assignments(self, table_node):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<field_assignments>"]:
            if self.current_tok in PREDICT_SET["<field_assignments>"]:
                field_name = self.get_current_token_value()
                self.parse_token("id")
                self.parse_token("=")
                value = self.value()
                self.parse_token(";")
                table_node.add_field(field_name, value)
                self.field_assignments(table_node)
            if self.current_tok in PREDICT_SET["<field_assignments_1>"]:
                log.info("Exit: " + self.current_tok)
                return
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<field_assignments>"])))
        log.info("Exit: " + self.current_tok)

    def flavor_tail(self):
        log.info("Enter: " + self.current_tok)
        arguments = []
        if self.current_tok in PREDICT_SET_ERR["<flavor_tail>"]:
            if self.current_tok in PREDICT_SET["<flavor_tail>"]:
                self.parse_token(",")
                arg = self.value()
                arguments.append(arg)
                more_args = self.flavor_tail()
                arguments.extend(more_args)
            if self.current_tok in PREDICT_SET["<flavor_tail_1>"]:
                log.info("Exit: " + self.current_tok)
                return []
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<flavor_tail>"])))
        log.info("Exit: " + self.current_tok)
        return arguments
        
    def built_in_rec_call(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<built-in_rec_call>"]:
            if self.current_tok in PREDICT_SET["<built-in_rec_call>"]:
                builtin_name = self.built_in_rec()
                arguments = self.tail1()
                return RecipeCall(builtin_name, arguments, [])
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<built-in_rec_call>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def built_in_rec(self):
        log.info("Enter: " + self.current_tok)
        builtin_name = None
        if self.current_tok in PREDICT_SET_ERR["<built-in_rec>"]:
            if self.current_tok in PREDICT_SET["<built-in_rec>"]:
                builtin_name = "append"
                self.parse_token("append")
            elif self.current_tok in PREDICT_SET["<built-in_rec_1>"]:
                builtin_name = "bill"
                self.parse_token("bill")
            elif self.current_tok in PREDICT_SET["<built-in_rec_2>"]:
                builtin_name = "copy"
                self.parse_token("copy")
            elif self.current_tok in PREDICT_SET["<built-in_rec_3>"]:
                builtin_name = "cut"
                self.parse_token("cut")
            elif self.current_tok in PREDICT_SET["<built-in_rec_4>"]:
                builtin_name = "fact"
                self.parse_token("fact")
            elif self.current_tok in PREDICT_SET["<built-in_rec_5>"]:
                builtin_name = "matches"
                self.parse_token("matches")
            elif self.current_tok in PREDICT_SET["<built-in_rec_6>"]:
                builtin_name = "pow"
                self.parse_token("pow")
            elif self.current_tok in PREDICT_SET["<built-in_rec_7>"]:
                builtin_name = "rand"
                self.parse_token("rand")
            elif self.current_tok in PREDICT_SET["<built-in_rec_8>"]:
                builtin_name = "remove"
                self.parse_token("remove")
            elif self.current_tok in PREDICT_SET["<built-in_rec_9>"]:
                builtin_name = "reverse"
                self.parse_token("reverse")
            elif self.current_tok in PREDICT_SET["<built-in_rec_10>"]:
                builtin_name = "search"
                self.parse_token("search")
            elif self.current_tok in PREDICT_SET["<built-in_rec_11>"]:
                builtin_name = "size"
                self.parse_token("size")
            elif self.current_tok in PREDICT_SET["<built-in_rec_12>"]:
                builtin_name = "sort"
                self.parse_token("sort")
            elif self.current_tok in PREDICT_SET["<built-in_rec_13>"]:
                builtin_name = "sqrt"
                self.parse_token("sqrt")
            elif self.current_tok in PREDICT_SET["<built-in_rec_14>"]:
                builtin_name = "take"
                self.parse_token("take")
            elif self.current_tok in PREDICT_SET["<built-in_rec_15>"]:
                builtin_name = "tochars"
                self.parse_token("tochars")
            elif self.current_tok in PREDICT_SET["<built-in_rec_16>"]:
                builtin_name = "topiece"
                self.parse_token("topiece")
            elif self.current_tok in PREDICT_SET["<built-in_rec_17>"]:
                builtin_name = "tosip"
                self.parse_token("tosip")
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<built-in_rec>"])))
        log.info("Exit: " + self.current_tok)
        return builtin_name

    def tail1(self):
        log.info("Enter: " + self.current_tok)
        arguments = []
        if self.current_tok in PREDICT_SET_ERR["<tail1>"]:
            if self.current_tok in PREDICT_SET["<tail1>"]:
                arguments = self.call_tail()
                # accessor_tail would be for if built-in returns array/table, but ignore for now
                self.accessor_tail()
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<tail1>"])))
        log.info("Exit: " + self.current_tok)
        return arguments

    def call_tail(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<call_tail>"]:
            if self.current_tok in PREDICT_SET["<call_tail>"]:
                self.parse_token("(")
                arguments = self.flavor()
                self.parse_token(")")
                return arguments
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<call_tail>"])))
        log.info("Exit: " + self.current_tok)
        return []
        
    def dimensions(self):
        log.info("Enter: " + self.current_tok)
        count = 0
        if self.current_tok in PREDICT_SET_ERR["<dimensions>"]:
            if self.current_tok in PREDICT_SET["<dimensions>"]:
                self.parse_token("[")
                self.parse_token("]")
                count = 1 + self.dimensions_tail()
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<dimensions>"])))
        log.info("Exit: " + self.current_tok)
        return count

    def dimensions_tail(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<dimensions_tail>"]:
            if self.current_tok in PREDICT_SET["<dimensions_tail>"]:
                return self.dimensions()
            if self.current_tok in PREDICT_SET["<dimensions_tail_1>"]:
                log.info("Exit: " + self.current_tok)
                return 0
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<dimensions_tail>"])))
        log.info("Exit: " + self.current_tok)
        return 0

    def array_declare(self):
        log.info("Enter: " + self.current_tok)
        id_and_inits = []
        if self.current_tok in PREDICT_SET_ERR["<array_declare>"]:
            if self.current_tok in PREDICT_SET["<array_declare>"]:
                identifier = self.get_current_token_value()
                self.parse_token("id")
                init_value = self.array_table_init()
                id_and_inits.append(IdAndInit(identifier, init_value))
                more_ids = self.array_declare_tail()
                id_and_inits.extend(more_ids)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<array_declare>"])))
        log.info("Exit: " + self.current_tok)
        return id_and_inits

    def array_table_init(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<array_table_init>"]:
            if self.current_tok in PREDICT_SET["<array_table_init>"]:
                self.parse_token("=")
                return self.value()
            if self.current_tok in PREDICT_SET["<array_table_init_1>"]:
                log.info("Exit: " + self.current_tok)
                return None
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<array_table_init>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def array_declare_tail(self):
        log.info("Enter: " + self.current_tok)
        id_and_inits = []
        if self.current_tok in PREDICT_SET_ERR["<array_declare_tail>"]:
            if self.current_tok in PREDICT_SET["<array_declare_tail>"]:
                self.parse_token(",")
                more_ids = self.array_declare()
                id_and_inits.extend(more_ids)
            if self.current_tok in PREDICT_SET["<array_declare_tail_1>"]:
                log.info("Exit: " + self.current_tok)
                return []
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<array_declare_tail>"])))
        log.info("Exit: " + self.current_tok)
        return id_and_inits

    def table_prototype(self):
        log.info("Enter: " + self.current_tok)
        table_decl = None
        if self.current_tok in PREDICT_SET_ERR["<table_prototype>"]:
            if self.current_tok in PREDICT_SET["<table_prototype>"]:
                self.parse_token("table")
                self.parse_token("of")
                table_name = self.get_current_token_value()
                self.parse_token("id")
                self.parse_token("=")
                self.parse_token("[")
                # Build TableDecl and populate with fields
                table_decl = TableDecl(table_name, [])
                self.required_decl(table_decl)
                self.parse_token("]")
                self.parse_token(";")
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<table_prototype>"])))
        log.info("Exit: " + self.current_tok)
        return table_decl

    def required_decl(self, table_decl_node=None):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<required_decl>"]:
            if self.current_tok in PREDICT_SET["<required_decl>"]:
                field_node = self.decl_head()
                if table_decl_node and field_node:
                    # Convert Spice to IngredientDecl for table field
                    field_decl = IngredientDecl(field_node.data_type, field_node.dimensions, [IdAndInit(field_node.identifier, None)])
                    table_decl_node.add_field(field_decl)
                self.parse_token(";")
                self.required_decl_tail(table_decl_node)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<required_decl>"])))
        log.info("Exit: " + self.current_tok)

    def decl_head(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<decl_head>"]:
            if self.current_tok in PREDICT_SET["<decl_head>"]:
                data_type, dimensions = self.primitive_types_dims()
                self.parse_token("of")
                identifier = self.get_current_token_value()
                self.parse_token("id")
                return Spice(data_type, dimensions, identifier)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<decl_head>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def primitive_types_dims(self):
        log.info("Enter: " + self.current_tok)
        data_type = None
        dimensions = 0
        if self.current_tok in PREDICT_SET_ERR["<primitive_types_dims>"]:
            if self.current_tok in PREDICT_SET["<primitive_types_dims>"]:
                data_type = "piece"
                self.parse_token("piece")
                dimensions = self.dimensions_tail()
            if self.current_tok in PREDICT_SET["<primitive_types_dims_1>"]:
                data_type = "sip"
                self.parse_token("sip")
                dimensions = self.dimensions_tail()
            if self.current_tok in PREDICT_SET["<primitive_types_dims_2>"]:
                data_type = "flag"
                self.parse_token("flag")
                dimensions = self.dimensions_tail()
            if self.current_tok in PREDICT_SET["<primitive_types_dims_3>"]:
                data_type = "chars"
                self.parse_token("chars")
                dimensions = self.dimensions_tail()
            if self.current_tok in PREDICT_SET["<primitive_types_dims_4>"]:
                # Table type (custom type)
                data_type = self.get_current_token_value()
                self.parse_token("id")
                dimensions = self.dimensions_tail()
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<primitive_types_dims>"])))
        log.info("Exit: " + self.current_tok)
        return (data_type, dimensions)
        
    def required_decl_tail(self, table_decl_node=None):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<required_decl_tail>"]:
            if self.current_tok in PREDICT_SET["<required_decl_tail>"]:
                self.required_decl(table_decl_node)
            if self.current_tok in PREDICT_SET["<required_decl_tail_1>"]:
                log.info("Exit: " + self.current_tok)
                return
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<required_decl_tail>"])))
        log.info("Exit: " + self.current_tok)
        
    def table_decl(self, table_name):
        log.info("Enter: " + self.current_tok)
        table_decl = None
        if self.current_tok in PREDICT_SET_ERR["<table_decl>"]:
            if self.current_tok in PREDICT_SET["<table_decl>"]:
                self.dimensions_tail()
                self.parse_token("of")
                self.table_declare()
                self.parse_token(";")
                # TODO: Build proper TableDecl with instances
                table_decl = TableDecl(table_name, [])
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<table_decl>"])))
        log.info("Exit: " + self.current_tok)
        return table_decl

    def table_declare(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<table_declare>"]:
            if self.current_tok in PREDICT_SET["<table_declare>"]:
                self.parse_token("id")
                self.array_table_init()
                self.table_declare_tail()
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<table_declare>"])))
        log.info("Exit: " + self.current_tok)

    def table_declare_tail(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<table_declare_tail>"]:
            if self.current_tok in PREDICT_SET["<table_declare_tail>"]:
                self.parse_token(",")
                self.table_declare()
            if self.current_tok in PREDICT_SET["<table_declare_tail_1>"]:
                log.info("Exit: " + self.current_tok)
                return
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<table_declare_tail>"])))
        log.info("Exit: " + self.current_tok)

    def recipe_decl(self, program_node):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<recipe_decl>"]:
            if self.current_tok in PREDICT_SET["<recipe_decl>"]:
                self.parse_token("prepare")
                return_type, recipe_name = self.serve_type()  # Parses "sip of main"
                self.parse_token("(")
                params = self.spice()
                self.parse_token(")")
                body = self.platter()
                # Create RecipeDecl node with correct order: serve_type, recipe_id, spices, platter
                recipe_node = RecipeDecl(return_type, recipe_name, params, body)
                program_node.add_recipe_decl(recipe_node)
                self.recipe_decl(program_node)
            if self.current_tok in PREDICT_SET["<recipe_decl_1>"]:
                log.info("Exit: " + self.current_tok)
                return
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<recipe_decl>"])))
        log.info("Exit: " + self.current_tok)

    def serve_type(self):
        log.info("Enter: " + self.current_tok)
        return_type = None
        recipe_name = None
        if self.current_tok in PREDICT_SET_ERR["<serve_type>"]:
            if self.current_tok in PREDICT_SET["<serve_type>"]:
                # serve_type is <decl_head> which parses: <primitive_types_dims> of id
                # This parses "sip of main" and returns (return_type, recipe_name)
                data_type, dimensions = self.primitive_types_dims()  # Parses "sip"
                self.parse_token("of")  # Parses "of"
                recipe_name = self.get_current_token_value()  # Get "main"
                self.parse_token("id")  # Parse the recipe name
                return_type = data_type
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<serve_type>"])))
        log.info("Exit: " + self.current_tok)
        return (return_type, recipe_name)

    def spice(self):
        log.info("Enter: " + self.current_tok)
        params = []
        if self.current_tok in PREDICT_SET_ERR["<spice>"]:
            if self.current_tok in PREDICT_SET["<spice>"]:
                # Build Spice nodes from parameters
                spice_node = self.decl_head()
                params.append(spice_node)
                more_params = self.spice_tail()
                params.extend(more_params)
            if self.current_tok in PREDICT_SET["<spice_1>"]:
                log.info("Exit: " + self.current_tok)
                return []
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<spice>"])))
        log.info("Exit: " + self.current_tok)
        return params
    
    def spice_tail(self):
        log.info("Enter: " + self.current_tok)
        params = []
        if self.current_tok in PREDICT_SET_ERR["<spice_tail>"]:
            if self.current_tok in PREDICT_SET["<spice_tail>"]:
                self.parse_token(",")
                spice_node = self.decl_head()
                params.append(spice_node)
                more_params = self.spice_tail()
                params.extend(more_params)
            if self.current_tok in PREDICT_SET["<spice_tail_1>"]:
                log.info("Exit: " + self.current_tok)
                return []
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<spice_tail>"])))
        log.info("Exit: " + self.current_tok)
        return params

    def platter(self):
        platter_node = Platter()
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<platter>"]:
            self.parse_token("{")
            self.local_decl(platter_node)
            self.statements(platter_node)
            self.parse_token("}")
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<platter>"])))
        log.info("Exit: " + self.current_tok)

        return platter_node


    def local_decl(self, platter_node):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<local_decl>"]:
            if self.current_tok in PREDICT_SET["<local_decl>"]:
                decl_node = self.decl_data_type()
                if decl_node:
                    platter_node.add_local_decl(decl_node)
                self.local_decl(platter_node)
            if self.current_tok in PREDICT_SET["<local_decl_1>"]:
                table_name = self.get_current_token_value()
                self.parse_token("id")
                self.local_id_tail(platter_node, table_name)
            if self.current_tok in PREDICT_SET["<local_decl_2>"]:
                log.info("Exit: " + self.current_tok)
                return
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<local_decl>"])))
        log.info("Exit: " + self.current_tok)

    def statements(self, platter_node):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<statements>"]:
            if self.current_tok in PREDICT_SET["<statements>"]:
                stmt_node = self.id_statements()
                if stmt_node:
                    platter_node.add_statement(stmt_node)
                self.statements(platter_node)
            if self.current_tok in PREDICT_SET["<statements_1>"]:
                builtin_call = self.built_in_rec_call()
                if builtin_call:
                    platter_node.add_statement(StandaloneRecipeCall(builtin_call))
                self.parse_token(";")
                self.statements(platter_node)
            if self.current_tok in PREDICT_SET["<statements_2>"]:
                cond_node = self.conditional_st()
                if cond_node:
                    platter_node.add_statement(cond_node)
                self.statements(platter_node)
            if self.current_tok in PREDICT_SET["<statements_3>"]:
                loop_node = self.looping_st()
                if loop_node:
                    platter_node.add_statement(loop_node)
                self.statements(platter_node)
            if self.current_tok in PREDICT_SET["<statements_4>"]:
                jump_node = self.jump_st()
                if jump_node:
                    platter_node.add_statement(jump_node)
                self.statements(platter_node)
            if self.current_tok in PREDICT_SET["<statements_5>"]:
                log.info("Exit: " + self.current_tok)
                return
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<statements>"])))
        log.info("Exit: " + self.current_tok)

    def local_id_tail(self, platter_node, table_name):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<local_id_tail>"]:
            if self.current_tok in PREDICT_SET["<local_id_tail>"]:
                # Table instance declaration: TableName of instance1, instance2;
                self.parse_token("of")
                # Build table instance declarations (not fully implemented - simplified)
                self.table_declare()
                self.parse_token(";")
                self.local_decl(platter_node)
            if self.current_tok in PREDICT_SET["<local_id_tail_1>"]:
                # Array table declaration
                self.parse_token("[")
                self.endb_tail(platter_node, table_name)
            if self.current_tok in PREDICT_SET["<local_id_tail_2>"]:
                # Statement: table access assignment
                indices = self.table_accessor()
                identifier_node = Identifier(table_name, indices)
                operator = self.assignment_op()
                value_node = self.value()
                assignment_node = Assignment(identifier_node, operator, value_node)
                platter_node.add_statement(assignment_node)
                self.parse_token(";")
                self.statements(platter_node)
            if self.current_tok in PREDICT_SET["<local_id_tail_3>"]:
                # Statement: simple assignment
                identifier_node = Identifier(table_name, [])
                operator = self.assignment_op()
                value_node = self.value()
                assignment_node = Assignment(identifier_node, operator, value_node)
                platter_node.add_statement(assignment_node)
                self.parse_token(";")
                self.statements(platter_node)
            if self.current_tok in PREDICT_SET["<local_id_tail_4>"]:
                # Statement: function call
                arguments = self.tail1()
                recipe_call_node = RecipeCall(table_name, arguments, [])
                platter_node.add_statement(StandaloneRecipeCall(recipe_call_node))
                self.parse_token(";")
                self.statements(platter_node)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<local_id_tail>"])))
        log.info("Exit: " + self.current_tok)

    def endb_tail(self, platter_node, identifier):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<]_tail>"]:
            if self.current_tok in PREDICT_SET["<]_tail>"]:
                # Array table declaration
                self.parse_token("]")
                self.dimensions_tail()
                self.parse_token("of")
                self.table_declare()
                self.parse_token(";")
                self.local_decl(platter_node)
            if self.current_tok in PREDICT_SET["<]_tail_1>"]:
                # Array access statement
                index_expr = self.expr()
                self.parse_token("]")
                more_indices = self.accessor_tail()
                indices = [index_expr] + more_indices
                identifier_node = Identifier(identifier, indices)
                operator = self.assignment_op()
                value_node = self.value()
                assignment_node = Assignment(identifier_node, operator, value_node)
                platter_node.add_statement(assignment_node)
                self.parse_token(";")
                self.statements(platter_node)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<]_tail>"])))
        log.info("Exit: " + self.current_tok)

    def id_statements(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<id_statements>"]:
            if self.current_tok in PREDICT_SET["<id_statements>"]:
                identifier = self.get_current_token_value()
                self.parse_token("id")
                return self.id_statements_ext(identifier)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<id_statements>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def id_statements_ext(self, identifier):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<id_statements_ext>"]:
            if self.current_tok in PREDICT_SET["<id_statements_ext>"]:
                # Function call
                arguments = self.tail1()
                recipe_call_node = RecipeCall(identifier, arguments, [])
                self.parse_token(";")
                return StandaloneRecipeCall(recipe_call_node)
            if self.current_tok in PREDICT_SET["<id_statements_ext_1>"]:
                # Assignment
                return self.assignment_st(identifier)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<id_statements_ext>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def assignment_st(self, identifier):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<assignment_st>"]:
            if self.current_tok in PREDICT_SET["<assignment_st>"]:
                indices = self.accessor_tail()
                identifier_node = Identifier(identifier, indices)
                operator = self.assignment_op()
                value_node = self.value()
                self.parse_token(";")
                return Assignment(identifier_node, operator, value_node)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<assignment_st>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def assignment_op(self):
        log.info("Enter: " + self.current_tok)
        operator = None
        if self.current_tok in PREDICT_SET_ERR["<assignment_op>"]:
            if self.current_tok in PREDICT_SET["<assignment_op>"]:
                operator = "="
                self.parse_token("=")
            if self.current_tok in PREDICT_SET["<assignment_op_1>"]:
                operator = "+="
                self.parse_token("+=")
            if self.current_tok in PREDICT_SET["<assignment_op_2>"]:
                operator = "-="
                self.parse_token("-=")
            if self.current_tok in PREDICT_SET["<assignment_op_3>"]:
                operator = "*="
                self.parse_token("*=")
            if self.current_tok in PREDICT_SET["<assignment_op_4>"]:
                operator = "/="
                self.parse_token("/=")
            if self.current_tok in PREDICT_SET["<assignment_op_5>"]:
                operator = "%="
                self.parse_token("%=")
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<assignment_op>"])))
        log.info("Exit: " + self.current_tok)
        return operator
    
    def conditional_st(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<conditional_st>"]:
            if self.current_tok in PREDICT_SET["<conditional_st>"]:
                return self.cond_check()
            if self.current_tok in PREDICT_SET["<conditional_st_1>"]:
                return self.cond_menu()
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<conditional_st>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def cond_check(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<cond_check>"]:
            if self.current_tok in PREDICT_SET["<cond_check>"]:
                self.parse_token("check")
                self.parse_token("(")
                condition = self.expr()
                self.parse_token(")")
                then_platter = self.platter()
                check_node = CheckStatement(condition, then_platter, [], None)
                self.alt_clause(check_node)
                self.instead_clause(check_node)
                return check_node
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<cond_check>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def alt_clause(self, check_node):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<alt_clause>"]:
            if self.current_tok in PREDICT_SET["<alt_clause>"]:
                self.parse_token("alt")
                self.parse_token("(")
                alt_condition = self.expr()
                self.parse_token(")")
                alt_platter = self.platter()
                check_node.add_alt(alt_condition, alt_platter)
                self.alt_clause(check_node)
            if self.current_tok in PREDICT_SET["<alt_clause_1>"]:
                log.info("Exit: " + self.current_tok)
                return
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<alt_clause>"])))
        log.info("Exit: " + self.current_tok)        

    def instead_clause(self, check_node):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<instead_clause>"]:
            if self.current_tok in PREDICT_SET["<instead_clause>"]:
                self.parse_token("instead")
                instead_platter = self.platter()
                check_node.set_instead(instead_platter)
            if self.current_tok in PREDICT_SET["<instead_clause_1>"]:
                log.info("Exit: " + self.current_tok)
                return
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<instead_clause>"])))
        log.info("Exit: " + self.current_tok)

    def cond_menu(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<cond_menu>"]:
            if self.current_tok in PREDICT_SET["<cond_menu>"]:
                self.parse_token("menu")
                self.parse_token("(")
                menu_value = self.expr()
                self.parse_token(")")
                menu_node = MenuStatement(menu_value, [], None)
                self.menu_platter(menu_node)
                return menu_node
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<cond_menu>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def menu_platter(self, menu_node):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<menu_platter>"]:
            if self.current_tok in PREDICT_SET["<menu_platter>"]:
                self.parse_token("{")
                self.choice_clause(menu_node)
                self.usual_clause(menu_node)
                self.parse_token("}")
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<menu_platter>"])))
        log.info("Exit: " + self.current_tok)

    def choice_clause(self, menu_node):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<choice_clause>"]:
            if self.current_tok in PREDICT_SET_ERR["<choice_clause>"]:
                self.parse_token("choice")
                choice_value = self.choice_val()
                self.parse_token(":")
                # Create a Platter for choice statements
                choice_platter = Platter()
                self.statements(choice_platter)
                menu_node.add_choice(choice_value, choice_platter)
                self.choice_clause(menu_node)
            if self.current_tok in PREDICT_SET["<choice_clause_1>"]:
                log.info("Exit: " + self.current_tok)
                return
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<choice_clause>"])))
        log.info("Exit: " + self.current_tok)

    def choice_val(self):
        log.info("Enter: " + self.current_tok)
        value = None
        if self.current_tok in PREDICT_SET_ERR["<choice_val>"]:
            if self.current_tok in PREDICT_SET["<choice_val>"]:
                value = self.get_current_token_value()
                self.parse_token("piece_lit")
                return Literal("piece_lit", value)
            if self.current_tok in PREDICT_SET["<choice_val_1>"]:
                value = self.get_current_token_value()
                self.parse_token("chars_lit")
                return Literal("chars_lit", value)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<choice_val>"])))
        log.info("Exit: " + self.current_tok)
        return None


    def usual_clause(self, menu_node):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<usual_clause>"]:
            if self.current_tok in PREDICT_SET["<usual_clause>"]:
                self.parse_token("usual")
                self.parse_token(":")
                # Create a Platter for usual statements
                usual_platter = Platter()
                self.statements(usual_platter)
                menu_node.set_usual(usual_platter)
            if self.current_tok in PREDICT_SET["<usual_clause_1>"]:
                log.info("Exit: " + self.current_tok)
                return
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<usual_clause>"])))
        log.info("Exit: " + self.current_tok)

    def looping_st(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<looping_st>"]:
            if self.current_tok in PREDICT_SET["<looping_st>"]:
                return self.loop_pass()
            if self.current_tok in PREDICT_SET["<looping_st_1>"]:
                return self.loop_repeat()
            if self.current_tok in PREDICT_SET["<looping_st_2>"]:
                return self.loop_order()
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<looping_st>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def loop_pass(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<loop_pass>"]:
            if self.current_tok in PREDICT_SET["<loop_pass>"]:
                self.parse_token("pass")
                self.parse_token("(")
                initialization = self.initialization()
                update = self.update()
                condition = self.expr()
                self.parse_token(")")
                body = self.platter()
                return PassLoop(initialization, condition, update, body)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<loop_pass>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def initialization(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<initialization>"]:
            if self.current_tok in PREDICT_SET["<initialization>"]:
                identifier = self.get_current_token_value()
                self.parse_token("id")
                init_value = self.ingredient_init()
                self.parse_token(";")
                # Build assignment for initialization
                identifier_node = Identifier(identifier, [])
                return Assignment(identifier_node, "=", init_value)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<initialization>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def update(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<update>"]:
            if self.current_tok in PREDICT_SET["<update>"]:
                identifier = self.get_current_token_value()
                self.parse_token("id")
                return self.assignment_st(identifier)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<update>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def loop_repeat(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<loop_repeat>"]:
            if self.current_tok in PREDICT_SET["<loop_repeat>"]:
                self.parse_token("repeat")
                self.parse_token("(")
                condition = self.expr()
                self.parse_token(")")
                body = self.platter()
                return RepeatLoop(condition, body)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<loop_repeat>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def loop_order(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<loop_order>"]:
            if self.current_tok in PREDICT_SET["<loop_order>"]:
                self.parse_token("order")
                body = self.platter()
                self.parse_token("repeat")
                self.parse_token("(")
                condition = self.expr()
                self.parse_token(")")
                self.parse_token(";")
                return OrderLoop(body, condition)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<loop_order>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def jump_st(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<jump_st>"]:
            if self.current_tok in PREDICT_SET["<jump_st>"]:
                return self.jump_next()
            if self.current_tok in PREDICT_SET["<jump_st_1>"]:
                return self.jump_stop()
            if self.current_tok in PREDICT_SET["<jump_st_2>"]:
                return self.jump_serve()
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<jump_st>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def jump_next(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<jump_next>"]:
            if self.current_tok in PREDICT_SET["<jump_next>"]:
                self.parse_token("next")
                self.parse_token(";")
                return NextStatement()
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<jump_next>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def jump_stop(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<jump_stop>"]:
            if self.current_tok in PREDICT_SET["<jump_stop>"]:
                self.parse_token("stop")
                self.parse_token(";")
                return StopStatement()
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<jump_stop>"])))
        log.info("Exit: " + self.current_tok)
        return None

    def jump_serve(self):
        log.info("Enter: " + self.current_tok)
        if self.current_tok in PREDICT_SET_ERR["<jump_serve>"]:
            if self.current_tok in PREDICT_SET["<jump_serve>"]:
                self.parse_token("serve")
                return_value = self.value()
                self.parse_token(";")
                return ServeStatement(return_value)
        else: self.error_handler("Unexpected_err", (", ".join(f"'{tok}'" for tok in PREDICT_SET_ERR["<jump_serve>"])))
        log.info("Exit: " + self.current_tok)
        return None


if __name__ == "__main__":
    # for debugging
    # code = """start();"""
    filename = "parser.platter"
    code = run_file(filename)
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    try:
        if parser.parse(): print("Syntax OK")
    except SyntaxError as e:
        print(str(e))
