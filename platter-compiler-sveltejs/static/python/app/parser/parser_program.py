from app.lexer.lexer import Lexer
from app.parser.error_handler import ErrorHandler
from app.parser.predict_set import PREDICT_SET
import logging as log

# To disable logs, set level=log.CRITICAL. 
# To enable logs, set level=log.DEBUG
log.basicConfig(level=log.DEBUG, format='%(levelname)s: <%(funcName)s> | %(message)s') # J

class Parser():
    def __init__(self, tokens):
        self.tokens = [t for t in tokens if t.type not in ("space", "tab", "newline", "comment_single", "comment_multi")] # filter out ws and comments
        if not self.tokens: 
            raise ErrorHandler("EOF", None, PREDICT_SET["<program>"])
        
        self.pos = 0
    
    def parse_token(self, tok):
        """Parse and consume a specific token type"""
        if self.pos >= len(self.tokens):
            raise ErrorHandler("EOF", None, tok)    
        
        if self.tokens[self.pos].type == tok: 
            log.warning(f"Expected: {tok} | Current: {self.tokens[self.pos].type} | Remark: MATCH!") # J
            self.pos += 1

        else:
            log.warning(f"Expected: {tok} | Current: {self.tokens[self.pos].type} | Remark: INVALID!\n") # J
            raise ErrorHandler("Unexpected_err", self.tokens[self.pos], tok)

    def parse_program(self):
        """ 1 <program> -> <global_decl> <recipe_decl> start() <platter>"""
        # Parse global declarations
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in PREDICT_SET["<global_decl>"]:
            self.global_decl()
        
        # Parse recipe declarations (prepare functions)
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in PREDICT_SET["<recipe_decl>"]:
            self.recipe_decl()

        # Parse start() platter
        if self.pos >= len(self.tokens):
            raise ErrorHandler("EOF", None, "start")
        
        self.parse_token("start")
        self.parse_token("(")
        self.parse_token(")")
        self.platter()
        
        # Ensure we've consumed all tokens
        if self.pos < len(self.tokens):
            raise ErrorHandler("ExpectedEOF_err", self.tokens[self.pos], None)
    
    def global_decl(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 2 <global_decl>	=>	piece	<piece_decl>	<global_decl> """
        """ 3 <global_decl>	=>	chars	<chars_decl>	<global_decl> """
        """ 4 <global_decl>	=>	sip	<sip_decl>	<global_decl> """
        """ 5 <global_decl>	=>	flag	<flag_decl>	<global_decl> """
        """ 6 <global_decl>	=>	<table_prototype>	<global_decl> """
        """ 7 <global_decl>	=>	id	<table_decl>	<global_decl> """
        """ 8 <global_decl>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_decl(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 9 <piece_decl>	=>	of	<piece_id>	; """
        """ 10 <piece_decl>	=>	<decl_type>	"""
        
        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_id(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J
        
        """ 11 <piece_id>	    =>	id	<piece_ingredient_init>	<piece_id_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_ingredient_init(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 12 <piece_ingredient_init>	=>	=	<strict_piece_expr> """
        """ 13 <piece_ingredient_init>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_piece_expr(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 14 <strict_piece_expr>	=>	<strict_piece_term>	<strict_piece_add_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_piece_term(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 15 <strict_piece_term>	=>	<strict_piece_factor>	<strict_piece_mult_tail>	<strict_piece_mult_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_piece_factor(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 16 <strict_piece_factor>	=>	<ret_piece> """
        """ 17 <strict_piece_factor>	=>	<id> """
        """ 18 <strict_piece_factor>	=>	(	<strict_piece_expr>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def ret_piece(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 19 <ret_piece>	=>	topiece	(	<any_expr>	) """
        """ 20 <ret_piece>	=>	size	(	<strict_array_expr>	) """
        """ 21 <ret_piece>	=>	search	(	<strict_array_expr>	,	<value>	) """
        """ 22 <ret_piece>	=>	fact	(	<strict_piece_expr>	) """
        """ 23 <ret_piece>	=>	pow	(	<strict_piece_expr>	,	<strict_piece_expr>	) """
        """ 24 <ret_piece>	=>	piece_lit """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def any_expr(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 25 <any_expr>	=>	<ret_piece>	<piece_mult_tail>	<piece_add_tail>	<piece_rel_gate> """
        """ 26 <any_expr>	=>	<ret_sip>	<sip_mult_tail>	<sip_add_tail>	<sip_rel_gate> """
        """ 27 <any_expr>	=>	<ret_chars>	<chars_add_tail>	<chars_rel_gate> """
        """ 28 <any_expr>	=>	<ret_flag>	<flag_logic_tail> """
        """ 29 <any_expr>	=>	<id>	<univ_mult_tail>	<univ_add_tail>	<univ_rel_gate> """
        """ 30 <any_expr>	=>	(	<paren_dispatch> """
        """ 31 <any_expr>	=>	not	<must_be_flag> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_mult_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 32 <piece_mult_tail>	=>	*	<piece_factor>	<piece_mult_tail> """
        """ 33 <piece_mult_tail>	=>	/	<piece_factor>	<piece_mult_tail> """
        """ 34 <piece_mult_tail>	=>	%	<piece_factor>	<piece_mult_tail> """
        """ 35 <piece_mult_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_factor(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 36 <piece_factor>	=>	<ret_piece> """
        """ 37 <piece_factor>	=>	<id> """
        """ 38 <piece_factor>	=>	(	<piece_inner_dispatch> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def id_symbol(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 39 <id>	=>	id	<id_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def id_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 40 <id_tail>	=>	<call_tailopt>	<accessor_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def call_tailopt(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 41 <call_tailopt>	=>	(	<flavor>	) """
        """ 42 <call_tailopt>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def flavor(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 43 <flavor>	=>	<value>	<flavor_tail> """
        """ 44 <flavor>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def value(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 45 <value>	=>	[	<notation_val>	] """
        """ 46 <value>	=>	<any_expr> """
        """ 47 <value>	=>	<ret_array> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def notation_val(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 48 <notation_val>	=>	<array_element> """
        """ 49 <notation_val>	=>	id	<array_or_table> """
        """ 50 <notation_val>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def array_element(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 51 <array_element>	=>	<ret_piece>	<element_value_tail> """
        """ 52 <array_element>	=>	<ret_sip>	<element_value_tail> """
        """ 53 <array_element>	=>	<ret_flag>	<element_value_tail> """
        """ 54 <array_element>	=>	<ret_chars>	<element_value_tail> """
        """ 55 <array_element>	=>	[	<notation_val>	]	<element_value_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def element_value_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 56 <element_value_tail>	=>	,	<array_element_id> """
        """ 57 <element_value_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def array_element_id(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 58 <array_element_id>	=>	id	<element_value_tail> """
        """ 59 <array_element_id>	=>	<array_element> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def ret_sip(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 60 <ret_sip>	=>	sqrt	(	<strict_piece_expr>	) """
        """ 61 <ret_sip>	=>	rand	( ) """
        """ 62 <ret_sip>	=>	tosip	(	<any_expr>	) """
        """ 63 <ret_sip>	=>	sip_lit """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def ret_flag(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 64 <ret_flag>	=>	matches	(	<strict_datas_expr>	,	<strict_datas_expr>	) """
        """ 65 <ret_flag>	=>	toflag	(	<any_expr>	) """
        """ 66 <ret_flag>	=>	flag_lit """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_datas_expr(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 67 <strict_datas_expr>	=>	[	<notation_val>	] """
        """ 68 <strict_datas_expr>	=>	<id> """
        """ 69 <strict_datas_expr>	=>	<ret_array> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def ret_array(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 70 <ret_array>	=>	append	(	<strict_array_expr>	,	<value>	) """
        """ 71 <ret_array>	=>	sort	(	<strict_array_expr>	) """
        """ 72 <ret_array>	=>	reverse	(	<strict_array_expr>	) """
        """ 73 <ret_array>	=>	remove	(	<strict_array_expr>	,	<value>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_array_expr(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 74 <strict_array_expr>	=>	[	<array_element_id>	] """
        """ 75 <strict_array_expr>	=>	<id> """
        """ 76 <strict_array_expr>	=>	<ret_array> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def ret_chars(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 77 <ret_chars>	=>	bill	(	<strict_chars_expr>	) """
        """ 78 <ret_chars>	=>	take	( ) """
        """ 79 <ret_chars>	=>	copy	(	<strict_chars_expr>	,	<strict_piece_expr>	,	<strict_piece_expr>	) """
        """ 80 <ret_chars>	=>	cut	(	<strict_piece_expr>	,	<strict_sip_expr>	) """
        """ 81 <ret_chars>	=>	tochars	(	<any_expr>	) """
        """ 82 <ret_chars>	=>	chars_lit """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_chars_expr(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 83 <strict_chars_expr>	=>	<strict_chars_factor>	<strict_chars_add_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_chars_factor(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 84 <strict_chars_factor>	=>	<ret_chars> """
        """ 85 <strict_chars_factor>	=>	<id> """
        """ 86 <strict_chars_factor>	=>	(	<strict_chars_expr>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_chars_add_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 87 <strict_chars_add_tail>	=>	+	<strict_chars_factor>	<strict_chars_add_tail> """
        """ 88 <strict_chars_add_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_sip_expr(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 89 <strict_sip_expr>	=>	<strict_sip_term>	<strict_sip_add_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_sip_term(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 90 <strict_sip_term>	=>	<strict_sip_factor>	<strict_sip_mult_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_sip_factor(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 91 <strict_sip_factor>	=>	<ret_sip> """
        """ 92 <strict_sip_factor>	=>	<id> """
        """ 93 <strict_sip_factor>	=>	(	<strict_sip_expr>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_sip_mult_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 94 <strict_sip_mult_tail>	=>	*	<strict_sip_factor>	<strict_sip_mult_tail> """
        """ 95 <strict_sip_mult_tail>	=>	/	<strict_sip_factor>	<strict_sip_mult_tail> """
        """ 96 <strict_sip_mult_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_sip_add_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 97 <strict_sip_add_tail>	=>	+	<strict_sip_term>	<strict_sip_add_tail> """
        """ 98 <strict_sip_add_tail>	=>	-	<strict_sip_term>	<strict_sip_add_tail> """
        """ 99 <strict_sip_add_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def array_or_table(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 100 <array_or_table>	=>	,	<array_element_id> """
        """ 101 <array_or_table>	=>	=	<value>	;	<field_assignments> """
        """ 102 <array_or_table>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def field_assignments(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 103 <field_assignments>	=>	id	=	<value>	;	<field_assignments> """
        """ 104 <field_assignments>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def flavor_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 105 <flavor_tail>	=>	,	<value>	<flavor_tail> """
        """ 106 <flavor_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def accessor_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 107 <accessor_tail>	=>	<array_accessor> """
        """ 108 <accessor_tail>	=>	<table_accessor> """
        """ 109 <accessor_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def array_accessor(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 110 <array_accessor>	=>	[	<strict_piece_expr>	]	<accessor_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def table_accessor(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 111 <table_accessor>	=>	:	id	<accessor_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_inner_dispatch(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 112 <piece_inner_dispatch>	=>	<ret_piece>	<piece_mult_tail>	<piece_add_tail>	<piece_bridge_recurse> """
        """ 113 <piece_inner_dispatch>	=>	<id>	<piece_mult_tail>	<piece_add_tail>	<piece_bridge_recurse> """
        """ 114 <piece_inner_dispatch>	=>	(	<piece_inner_dispatch>	<piece_close_recurse> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_add_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 115 <piece_add_tail>	=>	+	<piece_term>	<piece_add_tail> """
        """ 116 <piece_add_tail>	=>	-	<piece_term>	<piece_add_tail> """
        """ 117 <piece_add_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_term(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 118 <piece_term>	=>	<piece_factor>	<piece_mult_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_bridge_recurse(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 119 <piece_bridge_recurse>	=>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_close_recurse(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 120 <piece_close_recurse>	=>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_rel_gate(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 121 <piece_rel_gate>	=>	==	<piece_expr>	<flag_logic_tail> """
        """ 122 <piece_rel_gate>	=>	!=	<piece_expr>	<flag_logic_tail> """
        """ 123 <piece_rel_gate>	=>	<=	<piece_expr>	<flag_logic_tail> """
        """ 124 <piece_rel_gate>	=>	>=	<piece_expr>	<flag_logic_tail> """
        """ 125 <piece_rel_gate>	=>	<	<piece_expr>	<flag_logic_tail> """
        """ 126 <piece_rel_gate>	=>	>	<piece_expr>	<flag_logic_tail> """
        """ 127 <piece_rel_gate>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_expr(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 128 <piece_expr>	=>	<piece_term>	<piece_add_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def flag_logic_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 129 <flag_logic_tail>	=>	and	<must_be_flag> """
        """ 130 <flag_logic_tail>	=>	or	<must_be_flag> """
        """ 131 <flag_logic_tail>	=>	==	<must_be_flag> """
        """ 132 <flag_logic_tail>	=>	!=	<must_be_flag> """
        """ 133 <flag_logic_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def must_be_flag(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 134 <must_be_flag>	=>	<ret_piece>	<piece_mult_tail>	<piece_add_tail>	<piece_trap_gate> """
        """ 135 <must_be_flag>	=>	<ret_sip>	<sip_mult_tail>	<sip_add_tail>	<sip_trap_gate> """
        """ 136 <must_be_flag>	=>	<ret_chars>	<chars_add_tail>	<chars_trap_gate> """
        """ 137 <must_be_flag>	=>	<ret_flag>	<flag_logic_tail> """
        """ 138 <must_be_flag>	=>	<id>	<univ_mult_tail>	<univ_add_tail>	<univ_rel_gate> """
        """ 139 <must_be_flag>	=>	(	<paren_dispatch>	<flag_after_paren> """
        """ 140 <must_be_flag>	=>	not	<must_be_flag> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_trap_gate(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 141 <piece_trap_gate>	=>	==	<piece_expr>	<flag_logic_tail> """
        """ 142 <piece_trap_gate>	=>	!=	<piece_expr>	<flag_logic_tail> """
        """ 143 <piece_trap_gate>	=>	<=	<piece_expr>	<flag_logic_tail> """
        """ 144 <piece_trap_gate>	=>	>=	<piece_expr>	<flag_logic_tail> """
        """ 145 <piece_trap_gate>	=>	<	<piece_expr>	<flag_logic_tail> """
        """ 146 <piece_trap_gate>	=>	>	<piece_expr>	<flag_logic_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_mult_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 147 <sip_mult_tail>	=>	*	<sip_factor>	<sip_mult_tail> """
        """ 148 <sip_mult_tail>	=>	/	<sip_factor>	<sip_mult_tail> """
        """ 149 <sip_mult_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_factor(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 150 <sip_factor>	=>	<ret_sip> """
        """ 151 <sip_factor>	=>	<id> """
        """ 152 <sip_factor>	=>	(	<sip_inner_dispatch> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_inner_dispatch(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 153 <sip_inner_dispatch>	=>	<ret_sip>	<sip_mult_tail>	<sip_add_tail>	<sip_bridge_recurse> """
        """ 154 <sip_inner_dispatch>	=>	<id>	<sip_mult_tail>	<sip_add_tail>	<sip_bridge_recurse> """
        """ 155 <sip_inner_dispatch>	=>	(	<sip_inner_dispatch>	<sip_close_recurse> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_add_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 156 <sip_add_tail>	=>	+	<sip_term>	<sip_add_tail> """
        """ 157 <sip_add_tail>	=>	-	<sip_term>	<sip_add_tail> """
        """ 158 <sip_add_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_term(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 159 <sip_term>	=>	<sip_factor>	<sip_mult_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_bridge_recurse(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 160 <sip_bridge_recurse>	=>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_close_recurse(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 161 <sip_close_recurse>	=>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_trap_gate(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 162 <sip_trap_gate>	=>	==	<sip_expr>	<flag_logic_tail> """
        """ 163 <sip_trap_gate>	=>	!=	<sip_expr>	<flag_logic_tail> """
        """ 164 <sip_trap_gate>	=>	<=	<sip_expr>	<flag_logic_tail> """
        """ 165 <sip_trap_gate>	=>	>=	<sip_expr>	<flag_logic_tail> """
        """ 166 <sip_trap_gate>	=>	<	<sip_expr>	<flag_logic_tail> """
        """ 167 <sip_trap_gate>	=>	>	<sip_expr>	<flag_logic_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_expr(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 168 <sip_expr>	=>	<sip_term>	<sip_add_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def chars_add_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 169 <chars_add_tail>	=>	+	<chars_factor>	<chars_add_tail> """
        """ 170 <chars_add_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def chars_factor(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 171 <chars_factor>	=>	<ret_chars> """
        """ 172 <chars_factor>	=>	<id> """
        """ 173 <chars_factor>	=>	(	<chars_inner_dispatch> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def chars_inner_dispatch(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 174 <chars_inner_dispatch>	=>	<ret_chars>	<chars_add_tail>	<chars_bridge_recurse> """
        """ 175 <chars_inner_dispatch>	=>	<id>	<chars_add_tail>	<chars_bridge_recurse> """
        """ 176 <chars_inner_dispatch>	=>	(	<chars_inner_dispatch>	<chars_close_recurse> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def chars_bridge_recurse(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 177 <chars_bridge_recurse>	=>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def chars_close_recurse(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 178 <chars_close_recurse>	=>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def chars_trap_gate(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 179 <chars_trap_gate>	=>	==	<chars_expr>	<flag_logic_tail> """
        """ 180 <chars_trap_gate>	=>	!=	<chars_expr>	<flag_logic_tail> """
        """ 181 <chars_trap_gate>	=>	<=	<chars_expr>	<flag_logic_tail> """
        """ 182 <chars_trap_gate>	=>	>=	<chars_expr>	<flag_logic_tail> """
        """ 183 <chars_trap_gate>	=>	<	<chars_expr>	<flag_logic_tail> """
        """ 184 <chars_trap_gate>	=>	>	<chars_expr>	<flag_logic_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def chars_expr(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 185 <chars_expr>	=>	<chars_factor>	<chars_add_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def univ_mult_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 186 <univ_mult_tail>	=>	*	<univ_factor>	<univ_mult_tail> """
        """ 187 <univ_mult_tail>	=>	/	<univ_factor>	<univ_mult_tail> """
        """ 188 <univ_mult_tail>	=>	%	<univ_factor>	<univ_mult_tail> """
        """ 189 <univ_mult_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def univ_factor(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 190 <univ_factor>	=>	<id> """
        """ 191 <univ_factor>	=>	<ret_piece> """
        """ 192 <univ_factor>	=>	<ret_sip> """
        """ 193 <univ_factor>	=>	<ret_chars> """
        """ 194 <univ_factor>	=>	<ret_flag> """
        """ 195 <univ_factor>	=>	(	<any_expr>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def univ_add_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 196 <univ_add_tail>	=>	+	<univ_term>	<univ_add_tail> """
        """ 197 <univ_add_tail>	=>	-	<univ_term>	<univ_add_tail> """
        """ 198 <univ_add_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def univ_term(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 199 <univ_term>	=>	<univ_factor>	<univ_mult_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def univ_rel_gate(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 200 <univ_rel_gate>	=>	==	<univ_expr>	<flag_logic_tail> """
        """ 201 <univ_rel_gate>	=>	!=	<univ_expr>	<flag_logic_tail> """
        """ 202 <univ_rel_gate>	=>	<=	<univ_expr>	<flag_logic_tail> """
        """ 203 <univ_rel_gate>	=>	>=	<univ_expr>	<flag_logic_tail> """
        """ 204 <univ_rel_gate>	=>	<	<univ_expr>	<flag_logic_tail> """
        """ 205 <univ_rel_gate>	=>	>	<univ_expr>	<flag_logic_tail> """
        """ 206 <univ_rel_gate>	=>	and	<must_be_flag> """
        """ 207 <univ_rel_gate>	=>	or	<must_be_flag> """
        """ 208 <univ_rel_gate>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def univ_expr(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 209 <univ_expr>	=>	<univ_term>	<univ_add_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def paren_dispatch(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 210 <paren_dispatch>	=>	<ret_piece>	<piece_mult_tail>	<piece_add_tail>	<piece_bridge> """
        """ 211 <paren_dispatch>	=>	<ret_sip>	<sip_mult_tail>	<sip_add_tail>	<sip_bridge> """
        """ 212 <paren_dispatch>	=>	<ret_chars>	<chars_add_tail>	<chars_bridge> """
        """ 213 <paren_dispatch>	=>	<ret_flag>	<flag_logic_tail>	<flag_closure> """
        """ 214 <paren_dispatch>	=>	<id>	<univ_mult_tail>	<univ_add_tail>	<univ_bridge> """
        """ 215 <paren_dispatch>	=>	(	<paren_dispatch>	<univ_closure> """
        """ 216 <paren_dispatch>	=>	not	<must_be_flag>	<flag_closure> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_bridge(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 217 <piece_bridge>	=>	)	<piece_mult_tail>	<piece_add_tail>	<piece_rel_gate> """
        """ 218 <piece_bridge>	=>	==	<piece_expr>	<flag_logic_tail>	<flag_closure> """
        """ 219 <piece_bridge>	=>	!=	<piece_expr>	<flag_logic_tail>	<flag_closure> """
        """ 220 <piece_bridge>	=>	<=	<piece_expr>	<flag_logic_tail>	<flag_closure> """
        """ 221 <piece_bridge>	=>	>=	<piece_expr>	<flag_logic_tail>	<flag_closure> """
        """ 222 <piece_bridge>	=>	<	<piece_expr>	<flag_logic_tail>	<flag_closure> """
        """ 223 <piece_bridge>	=>	>	<piece_expr>	<flag_logic_tail>	<flag_closure> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def flag_closure(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 224 <flag_closure>	=>	)	<flag_logic_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_bridge(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 225 <sip_bridge>	=>	)	<sip_mult_tail>	<sip_add_tail>	<sip_rel_gate> """
        """ 226 <sip_bridge>	=>	==	<sip_expr>	<flag_logic_tail>	<flag_closure> """
        """ 227 <sip_bridge>	=>	!=	<sip_expr>	<flag_logic_tail>	<flag_closure> """
        """ 228 <sip_bridge>	=>	<=	<sip_expr>	<flag_logic_tail>	<flag_closure> """
        """ 229 <sip_bridge>	=>	>=	<sip_expr>	<flag_logic_tail>	<flag_closure> """
        """ 230 <sip_bridge>	=>	<	<sip_expr>	<flag_logic_tail>	<flag_closure> """
        """ 231 <sip_bridge>	=>	>	<sip_expr>	<flag_logic_tail>	<flag_closure> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_rel_gate(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 232 <sip_rel_gate>	=>	==	<sip_expr>	<flag_logic_tail> """
        """ 233 <sip_rel_gate>	=>	!=	<sip_expr>	<flag_logic_tail> """
        """ 234 <sip_rel_gate>	=>	<=	<sip_expr>	<flag_logic_tail> """
        """ 235 <sip_rel_gate>	=>	>=	<sip_expr>	<flag_logic_tail> """
        """ 236 <sip_rel_gate>	=>	<	<sip_expr>	<flag_logic_tail> """
        """ 237 <sip_rel_gate>	=>	>	<sip_expr>	<flag_logic_tail> """
        """ 238 <sip_rel_gate>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def chars_bridge(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 239 <chars_bridge>	=>	)	<chars_add_tail>	<chars_rel_gate> """
        """ 240 <chars_bridge>	=>	==	<chars_expr>	<flag_logic_tail>	<flag_closure> """
        """ 241 <chars_bridge>	=>	<=	<chars_expr>	<flag_logic_tail>	<flag_closure> """
        """ 242 <chars_bridge>	=>	>=	<chars_expr>	<flag_logic_tail>	<flag_closure> """
        """ 243 <chars_bridge>	=>	<	<chars_expr>	<flag_logic_tail>	<flag_closure> """
        """ 244 <chars_bridge>	=>	>	<chars_expr>	<flag_logic_tail>	<flag_closure> """
        """ 245 <chars_bridge>	=>	!=	<chars_expr>	<flag_logic_tail>	<flag_closure> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def chars_rel_gate(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 246 <chars_rel_gate>	=>	<=	<chars_expr>	<flag_logic_tail> """
        """ 247 <chars_rel_gate>	=>	>=	<chars_expr>	<flag_logic_tail> """
        """ 248 <chars_rel_gate>	=>	<	<chars_expr>	<flag_logic_tail> """
        """ 249 <chars_rel_gate>	=>	>	<chars_expr>	<flag_logic_tail> """
        """ 250 <chars_rel_gate>	=>	==	<chars_expr>	<flag_logic_tail> """
        """ 251 <chars_rel_gate>	=>	!=	<chars_expr>	<flag_logic_tail> """
        """ 252 <chars_rel_gate>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def univ_bridge(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 253 <univ_bridge>	=>	)	<univ_mult_tail>	<univ_add_tail>	<univ_rel_gate> """
        """ 254 <univ_bridge>	=>	==	<univ_expr>	<flag_logic_tail>	<flag_closure> """
        """ 255 <univ_bridge>	=>	!=	<univ_expr>	<flag_logic_tail>	<flag_closure> """
        """ 256 <univ_bridge>	=>	<=	<univ_expr>	<flag_logic_tail>	<flag_closure> """
        """ 257 <univ_bridge>	=>	>=	<univ_expr>	<flag_logic_tail>	<flag_closure> """
        """ 258 <univ_bridge>	=>	<	<univ_expr>	<flag_logic_tail>	<flag_closure> """
        """ 259 <univ_bridge>	=>	>	<univ_expr>	<flag_logic_tail>	<flag_closure> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def univ_closure(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 260 <univ_closure>	=>	)	<univ_mult_tail>	<univ_add_tail>	<univ_rel_gate> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def flag_after_paren(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 261 <flag_after_paren>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_piece_mult_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 262 <strict_piece_mult_tail>	=>	*	<strict_piece_factor>	<strict_piece_mult_tail> """
        """ 263 <strict_piece_mult_tail>	=>	/	<strict_piece_factor>	<strict_piece_mult_tail> """
        """ 264 <strict_piece_mult_tail>	=>	%	<strict_piece_factor>	<strict_piece_mult_tail> """
        """ 265 <strict_piece_mult_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_piece_add_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 266 <strict_piece_add_tail>	=>	+	<strict_piece_term>	<strict_piece_add_tail> """
        """ 267 <strict_piece_add_tail>	=>	-	<strict_piece_term>	<strict_piece_add_tail> """
        """ 268 <strict_piece_add_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def piece_id_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 269 <piece_id_tail>	=>	,	id	<piece_ingredient_init>	<piece_id_tail> """
        """ 270 <piece_id_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def decl_type(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 271 <decl_type>	=>	<dimensions>	of	<array_declare>	; """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def dimensions(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 272 <dimensions>	=>	[	]	<dimensions_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def dimensions_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 273 <dimensions_tail>	=>	<dimensions> """
        """ 274 <dimensions_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def array_declare(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 275 <array_declare>	=>	id	<array_init>	<array_declare_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def array_init(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 276 <array_init>	=>	=	<strict_array_expr> """
        """ 277 <array_init>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def array_declare_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 278 <array_declare_tail>	=>	,	<array_declare> """
        """ 279 <array_declare_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def chars_id(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 282 <chars_id>	=>	id	<chars_ingredient_init>	<chars_id_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def chars_ingredient_init(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 283 <chars_ingredient_init>	=>	=	<strict_chars_expr> """
        """ 284 <chars_ingredient_init>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def chars_id_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 285 <chars_id_tail>	=>	,	id	<chars_ingredient_init>	<chars_id_tail> """
        """ 286 <chars_id_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_id(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 289 <sip_id>	=>	id	<sip_ingredient_init>	<sip_id_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_ingredient_init(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 290 <sip_ingredient_init>	=>	=	<strict_sip_expr> """
        """ 291 <sip_ingredient_init>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def sip_id_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 292 <sip_id_tail>	=>	,	id	<sip_ingredient_init>	<sip_id_tail> """
        """ 293 <sip_id_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def flag_id(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 296 <flag_id>	=>	id	<flag_ingredient_init>	<flag_id_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def flag_ingredient_init(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 297 <flag_ingredient_init>	=>	=	<strict_flag_expr> """
        """ 298 <flag_ingredient_init>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_flag_expr(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 299 <strict_flag_expr>	=>	<strict_flag_term>	<strict_flag_or_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_flag_term(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 300 <strict_flag_term>	=>	<strict_flag_equality>	<strict_flag_and_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_flag_equality(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 301 <strict_flag_equality>	=>	<strict_flag_factor>	<strict_flag_eq_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_flag_factor(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 302 <strict_flag_factor>	=>	<ret_flag> """
        """ 303 <strict_flag_factor>	=>	not	<strict_flag_factor> """
        """ 304 <strict_flag_factor>	=>	<id>	<strict_id_master_tail> """
        """ 305 <strict_flag_factor>	=>	(	<strict_flag_paren_entry> """
        """ 306 <strict_flag_factor>	=>	<ret_piece>	<piece_mult_tail>	<piece_add_tail>	<strict_piece_gate> """
        """ 307 <strict_flag_factor>	=>	<ret_sip>	<sip_mult_tail>	<sip_add_tail>	<strict_sip_gate> """
        """ 308 <strict_flag_factor>	=>	<ret_chars>	<chars_add_tail>	<strict_chars_gate> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_id_master_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 309 <strict_id_master_tail>	=>	*	<univ_factor>	<univ_mult_tail>	<univ_add_tail>	<strict_forced_gate> """
        """ 310 <strict_id_master_tail>	=>	/	<univ_factor>	<univ_mult_tail>	<univ_add_tail>	<strict_forced_gate> """
        """ 311 <strict_id_master_tail>	=>	%	<univ_factor>	<univ_mult_tail>	<univ_add_tail>	<strict_forced_gate> """
        """ 312 <strict_id_master_tail>	=>	+	<univ_term>	<univ_add_tail>	<strict_forced_gate> """
        """ 313 <strict_id_master_tail>	=>	-	<univ_term>	<univ_add_tail>	<strict_forced_gate> """
        """ 314 <strict_id_master_tail>	=>	==	<univ_expr> """
        """ 315 <strict_id_master_tail>	=>	!=	<univ_expr> """
        """ 316 <strict_id_master_tail>	=>	<=	<comparable_expr> """
        """ 317 <strict_id_master_tail>	=>	>=	<comparable_expr> """
        """ 318 <strict_id_master_tail>	=>	<	<comparable_expr> """
        """ 319 <strict_id_master_tail>	=>	>	<comparable_expr> """
        """ 320 <strict_id_master_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_forced_gate(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 321 <strict_forced_gate>	=>	==	<univ_expr> """
        """ 322 <strict_forced_gate>	=>	!=	<univ_expr> """
        """ 323 <strict_forced_gate>	=>	<=	<univ_expr> """
        """ 324 <strict_forced_gate>	=>	>=	<univ_expr> """
        """ 325 <strict_forced_gate>	=>	<	<univ_expr> """
        """ 326 <strict_forced_gate>	=>	>	<univ_expr> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def comparable_expr(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 327 <comparable_expr>	=>	<comparable_term>	<comparable_add_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def comparable_term(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 328 <comparable_term>	=>	<comparable_factor>	<comparable_mult_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def comparable_factor(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 329 <comparable_factor>	=>	<id> """
        """ 330 <comparable_factor>	=>	<ret_piece> """
        """ 331 <comparable_factor>	=>	<ret_sip> """
        """ 332 <comparable_factor>	=>	<ret_chars> """
        """ 333 <comparable_factor>	=>	(	<any_expr>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def comparable_mult_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 334 <comparable_mult_tail>	=>	*	<comparable_factor>	<comparable_mult_tail> """
        """ 335 <comparable_mult_tail>	=>	/	<comparable_factor>	<comparable_mult_tail> """
        """ 336 <comparable_mult_tail>	=>	%	<comparable_factor>	<comparable_mult_tail> """
        """ 337 <comparable_mult_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def comparable_add_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 338 <comparable_add_tail>	=>	+	<comparable_term>	<comparable_add_tail> """
        """ 339 <comparable_add_tail>	=>	-	<comparable_term>	<comparable_add_tail> """
        """ 340 <comparable_add_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_flag_paren_entry(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 341 <strict_flag_paren_entry>	=>	<ret_piece>	<piece_mult_tail>	<piece_add_tail>	<strict_paren_piece_bridge> """
        """ 342 <strict_flag_paren_entry>	=>	<ret_sip>	<sip_mult_tail>	<sip_add_tail>	<strict_paren_sip_bridge> """
        """ 343 <strict_flag_paren_entry>	=>	<ret_chars>	<chars_add_tail>	<strict_paren_chars_bridge> """
        """ 344 <strict_flag_paren_entry>	=>	<ret_flag>	<flag_logic_tail>	<strict_paren_flag_bridge> """
        """ 345 <strict_flag_paren_entry>	=>	not	<must_be_flag>	<strict_paren_flag_bridge> """
        """ 346 <strict_flag_paren_entry>	=>	<id>	<univ_mult_tail>	<univ_add_tail>	<strict_paren_univ_bridge> """
        """ 347 <strict_flag_paren_entry>	=>	(	<strict_flag_paren_entry>	<strict_paren_univ_bridge> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_paren_piece_bridge(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 348 <strict_paren_piece_bridge>	=>	)	<piece_mult_tail>	<piece_add_tail>	<strict_piece_gate> """
        """ 349 <strict_paren_piece_bridge>	=>	<strict_piece_gate>	<flag_logic_tail>	<strict_paren_flag_bridge> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_piece_gate(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 350 <strict_piece_gate>	=>	==	<piece_expr> """
        """ 351 <strict_piece_gate>	=>	!=	<piece_expr> """
        """ 352 <strict_piece_gate>	=>	<=	<piece_expr> """
        """ 353 <strict_piece_gate>	=>	>=	<piece_expr> """
        """ 354 <strict_piece_gate>	=>	<	<piece_expr> """
        """ 355 <strict_piece_gate>	=>	>	<piece_expr> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_paren_flag_bridge(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 356 <strict_paren_flag_bridge>	=>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_paren_sip_bridge(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 357 <strict_paren_sip_bridge>	=>	)	<sip_mult_tail>	<sip_add_tail>	<strict_sip_gate> """
        """ 358 <strict_paren_sip_bridge>	=>	<strict_sip_gate>	<flag_logic_tail>	<strict_paren_flag_bridge> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_sip_gate(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 359 <strict_sip_gate>	=>	==	<sip_expr> """
        """ 360 <strict_sip_gate>	=>	!=	<sip_expr> """
        """ 361 <strict_sip_gate>	=>	<=	<sip_expr> """
        """ 362 <strict_sip_gate>	=>	>=	<sip_expr> """
        """ 363 <strict_sip_gate>	=>	<	<sip_expr> """
        """ 364 <strict_sip_gate>	=>	>	<sip_expr> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_paren_chars_bridge(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 365 <strict_paren_chars_bridge>	=>	)	<chars_add_tail>	<strict_chars_gate> """
        """ 366 <strict_paren_chars_bridge>	=>	<strict_chars_gate>	<flag_logic_tail>	<strict_paren_flag_bridge> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_chars_gate(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 367 <strict_chars_gate>	=>	<=	<chars_expr> """
        """ 368 <strict_chars_gate>	=>	>=	<chars_expr> """
        """ 369 <strict_chars_gate>	=>	<	<chars_expr> """
        """ 370 <strict_chars_gate>	=>	>	<chars_expr> """
        """ 371 <strict_chars_gate>	=>	==	<chars_expr> """
        """ 372 <strict_chars_gate>	=>	!=	<chars_expr> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_paren_univ_bridge(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 373 <strict_paren_univ_bridge>	=>	)	<univ_mult_tail>	<univ_add_tail>	<strict_forced_gate> """
        """ 374 <strict_paren_univ_bridge>	=>	<strict_forced_gate>	<flag_logic_tail>	<strict_paren_flag_bridge> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_flag_eq_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 375 <strict_flag_eq_tail>	=>	==	<strict_flag_equality> """
        """ 376 <strict_flag_eq_tail>	=>	!=	<strict_flag_equality> """
        """ 377 <strict_flag_eq_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_flag_and_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 378 <strict_flag_and_tail>	=>	and	<strict_flag_equality>	<strict_flag_and_tail> """
        """ 379 <strict_flag_and_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_flag_or_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 380 <strict_flag_or_tail>	=>	or	<strict_flag_term>	<strict_flag_or_tail> """
        """ 381 <strict_flag_or_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def flag_id_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 382 <flag_id_tail>	=>	,	id	<flag_ingredient_init>	<flag_id_tail> """
        """ 383 <flag_id_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def required_decl(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 385 <required_decl>	=>	<decl_head>	;	<required_decl_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def decl_head(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 386 <decl_head>	=>	<primitive_types_dims>	of	id """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def primitive_types_dims(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 387 <primitive_types_dims>	=>	piece	<dimensions_tail> """
        """ 388 <primitive_types_dims>	=>	sip	<dimensions_tail> """
        """ 389 <primitive_types_dims>	=>	flag	<dimensions_tail> """
        """ 390 <primitive_types_dims>	=>	chars	<dimensions_tail> """
        """ 391 <primitive_types_dims>	=>	id	<dimensions_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def required_decl_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 392 <required_decl_tail>	=>	<required_decl> """
        """ 393 <required_decl_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def table_declare(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 396 <table_declare>	=>	id	<table_init>	<table_declare_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def table_init(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 397 <table_init>	=>	=	<strict_table_expr> """
        """ 398 <table_init>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def strict_table_expr(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 399 <strict_table_expr>	=>	[	<field_assignments>	] """
        """ 400 <strict_table_expr>	=>	<id> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def table_declare_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 401 <table_declare_tail>	=>	,	<table_declare> """
        """ 402 <table_declare_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def table_prototype(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 384 <table_prototype>	=>	table	of	id	=	[	<required_decl>	]	; """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def table_decl(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 394 <table_decl>	=>	of	<table_declare>	; """
        """ 395 <table_decl>	=>	<decl_type> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def serve_type(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 405 <serve_type>	=>	<decl_head> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def spice(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 406 <spice>	=>	<decl_head>	<spice_tail> """
        """ 407 <spice>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def spice_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 408 <spice_tail>	=>	,	<decl_head>	<spice_tail> """
        """ 409 <spice_tail>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def recipe_decl(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 403 <recipe_decl>	=>	prepare	<serve_type>	(	<spice>	)	<platter>	<recipe_decl> """
        """ 404 <recipe_decl>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def local_decl(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 411 <local_decl>	=>	piece	<piece_decl>	<local_decl> """
        """ 412 <local_decl>	=>	chars	<chars_decl>	<local_decl> """
        """ 413 <local_decl>	=>	sip	<sip_decl>	<local_decl> """
        """ 414 <local_decl>	=>	flag	<flag_decl>	<local_decl> """
        """ 415 <local_decl>	=>	id	<local_id_tail> """
        """ 416 <local_decl>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def local_id_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 417 <local_id_tail>	=>	of	<table_declare>	;	<local_decl> """
        """ 418 <local_id_tail>	=>	[	<endb_tail> """
        """ 419 <local_id_tail>	=>	<table_accessor>	<assignment_op>	<value>	;	<statements> """
        """ 420 <local_id_tail>	=>	<assignment_op>	<value>	;	<statements> """
        """ 421 <local_id_tail>	=>	<tail1>	;	<statements> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def endb_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 422 <endb_tail>	=>	]	<dimensions_tail>	of	<array_declare>	;	<local_decl> """
        """ 423 <endb_tail>	=>	<strict_piece_expr>	]	<accessor_tail>	<assignment_op>	<value>	;	<statements> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def assignment_op(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 424 <assignment_op>	=>	= """
        """ 425 <assignment_op>	=>	+= """
        """ 426 <assignment_op>	=>	-= """
        """ 427 <assignment_op>	=>	*= """
        """ 428 <assignment_op>	=>	/= """
        """ 429 <assignment_op>	=>	%= """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def statements(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 430 <statements>	=>	<id_statements>	<statements> """
        """ 431 <statements>	=>	<built_in_rec_call>	;	<statements> """
        """ 432 <statements>	=>	<conditional_st>	<statements> """
        """ 433 <statements>	=>	<looping_st>	<statements> """
        """ 434 <statements>	=>	<jump_serve>	<statements> """
        """ 435 <statements>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def id_statements(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 436 <id_statements>	=>	id	<id_statements_ext>	<statements> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def id_statements_ext(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 437 <id_statements_ext>	=>	<tail1>	; """
        """ 438 <id_statements_ext>	=>	<assignment_st> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def tail1(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 439 <tail1>	=>	<call_tail>	<accessor_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def call_tail(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 440 <call_tail>	=>	(	<flavor>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def assignment_st(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 441 <assignment_st>	=>	<accessor_tail>	<assignment_op>	<value>	; """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def built_in_rec_call(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 442 <built_in_rec_call>	=>	<built_in_rec>	<accessor_tail> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def built_in_rec(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 443 <built_in_rec>	=>	append	(	<strict_array_expr>	,	<value>	) """
        """ 444 <built_in_rec>	=>	bill	(	<strict_chars_expr>	) """
        """ 445 <built_in_rec>	=>	copy	(	<strict_chars_expr>	,	<strict_piece_expr>	,	<strict_piece_expr>	) """
        """ 446 <built_in_rec>	=>	cut	(	<strict_piece_expr>	,	<strict_sip_expr>	) """
        """ 447 <built_in_rec>	=>	fact	(	<strict_piece_expr>	) """
        """ 448 <built_in_rec>	=>	matches	(	<strict_datas_expr>	,	<strict_datas_expr>	) """
        """ 449 <built_in_rec>	=>	pow	(	<strict_piece_expr>	,	<strict_piece_expr>	) """
        """ 450 <built_in_rec>	=>	rand	(	) """
        """ 451 <built_in_rec>	=>	remove	(	<strict_array_expr>	,	<value>	) """
        """ 452 <built_in_rec>	=>	reverse	(	<strict_array_expr>	) """
        """ 453 <built_in_rec>	=>	search	(	<strict_array_expr>	,	<value>	) """
        """ 454 <built_in_rec>	=>	size	(	<strict_array_expr>	) """
        """ 455 <built_in_rec>	=>	sort	(	<strict_array_expr>	) """
        """ 456 <built_in_rec>	=>	sqrt	(	<strict_piece_expr>	) """
        """ 457 <built_in_rec>	=>	take	(	) """
        """ 458 <built_in_rec>	=>	tochars	(	<any_expr>	) """
        """ 459 <built_in_rec>	=>	topiece	(	<any_expr>	) """
        """ 460 <built_in_rec>	=>	tosip	(	<any_expr>	) """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def conditional_st(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 461 <conditional_st>	=>	<cond_check> """
        """ 462 <conditional_st>	=>	<cond_menu> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def cond_check(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 463 <cond_check>	=>	check	(	<strict_flag_expr>	)	<platter>	<alt_clause>	<instead_clause> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def alt_clause(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 464 <alt_clause>	=>	alt	(	<strict_flag_expr>	)	<platter>	<alt_clause> """
        """ 465 <alt_clause>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def instead_clause(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 466 <instead_clause>	=>	instead	<platter> """
        """ 467 <instead_clause>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def cond_menu(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 468 <cond_menu>	=>	menu	(	<any_expr>	)	<menu_platter> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def menu_platter(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 469 <menu_platter>	=>	{	<choice_clause>	<usual_clause>	} """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def choice_clause(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 470 <choice_clause>	=>	choice	<choice_val>	:	<statements_menu>	<choice_clause> """
        """ 471 <choice_clause>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def choice_val(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 472 <choice_val>	=>	piece_lit """
        """ 473 <choice_val>	=>	chars_lit """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def statements_menu(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 474 <statements_menu>	=>	<id_statements_menu>	<statements_menu> """
        """ 475 <statements_menu>	=>	<built_in_rec_call>	;	<statements_menu> """
        """ 476 <statements_menu>	=>	<conditional_st_menu>	<statements_menu> """
        """ 477 <statements_menu>	=>	<looping_st>	<statements_menu> """
        """ 478 <statements_menu>	=>	<jump_stop>	<statements_menu> """
        """ 479 <statements_menu>	=>	<jump_serve>	<statements_menu> """
        """ 480 <statements_menu>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def id_statements_menu(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 481 <id_statements_menu>	=>	id	<id_statements_ext>	<statements_menu> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def conditional_st_menu(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 482 <conditional_st_menu>	=>	<cond_check_menu> """
        """ 483 <conditional_st_menu>	=>	<cond_menu> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def cond_check_menu(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 484 <cond_check_menu>	=>	check	(	<strict_flag_expr>	)	<endb_menu_check_platter>	<alt_clause>	<instead_clause> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def endb_menu_check_platter(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 485 <endb_menu_check_platter>	=>	{	<local_decl_menu>	<statements_menu>	} """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def local_decl_menu(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 486 <local_decl_menu>	=>	piece	<piece_decl>	<local_decl_menu> """
        """ 487 <local_decl_menu>	=>	chars	<chars_decl>	<local_decl_menu> """
        """ 488 <local_decl_menu>	=>	sip	<sip_decl>	<local_decl_menu> """
        """ 489 <local_decl_menu>	=>	flag	<flag_decl>	<local_decl_menu> """
        """ 490 <local_decl_menu>	=>	id	<local_id_tail_menu> """
        """ 491 <local_decl_menu>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def local_id_tail_menu(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 492 <local_id_tail_menu>	=>	of	<table_declare>	;	<local_decl_menu> """
        """ 493 <local_id_tail_menu>	=>	[	<endb_tail_menu> """
        """ 494 <local_id_tail_menu>	=>	<table_accessor>	<assignment_op>	<value>	;	<statements_menu> """
        """ 495 <local_id_tail_menu>	=>	<assignment_op>	<value>	;	<statements_menu> """
        """ 496 <local_id_tail_menu>	=>	<tail1>	;	<statements_menu> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def endb_tail_menu(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 497 <endb_tail_menu>	=>	]	<dimensions_tail>	of	<table_declare>	;	<local_decl_menu> """
        """ 498 <endb_tail_menu>	=>	<strict_piece_expr>	]	<accessor_tail>	<assignment_op>	<value>	;	<statements_menu> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def platter(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 410 <platter>	=>	{	<local_decl>	<statements>	} """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def looping_st(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 499 <looping_st>	=>	<loop_pass> """
        """ 500 <looping_st>	=>	<loop_repeat> """
        """ 501 <looping_st>	=>	<loop_order> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def loop_pass(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 502 <loop_pass>	=>	pass	(	<initialization>	<update>	<strict_flag_expr>	)	<endb_loop_platter> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def initialization(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 503 <initialization>	=>	id	=	<strict_piece_expr>	; """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def update(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 504 <update>	=>	id	<assignment_st> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def endb_loop_platter(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 505 <endb_loop_platter>	=>	{	<local_decl_loop>	<statements_loop>	} """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def local_decl_loop(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 506 <local_decl_loop>	=>	piece	<piece_decl>	<local_decl_loop> """
        """ 507 <local_decl_loop>	=>	chars	<chars_decl>	<local_decl_loop> """
        """ 508 <local_decl_loop>	=>	sip	<sip_decl>	<local_decl_loop> """
        """ 509 <local_decl_loop>	=>	flag	<flag_decl>	<local_decl_loop> """
        """ 510 <local_decl_loop>	=>	id	<local_id_tail_loop> """
        """ 511 <local_decl_loop>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def local_id_tail_loop(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 512 <local_id_tail_loop>	=>	of	<table_declare>	;	<local_decl_loop> """
        """ 513 <local_id_tail_loop>	=>	[	<endb_tail_loop> """
        """ 514 <local_id_tail_loop>	=>	<table_accessor>	<assignment_op>	<value>	;	<statements_loop> """
        """ 515 <local_id_tail_loop>	=>	<assignment_op>	<value>	;	<statements_loop> """
        """ 516 <local_id_tail_loop>	=>	<tail1>	;	<statements_loop> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def endb_tail_loop(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 517 <endb_tail_loop>	=>	]	<dimensions_tail>	of	<table_declare>	;	<local_decl_loop> """
        """ 518 <endb_tail_loop>	=>	<strict_piece_expr>	]	<accessor_tail>	<assignment_op>	<value>	;	<statements_loop> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def statements_loop(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 519 <statements_loop>	=>	<id_statements_loop>	<statements_loop> """
        """ 520 <statements_loop>	=>	<built_in_rec_call>	;	<statements_loop> """
        """ 521 <statements_loop>	=>	<conditional_st_loop>	<statements_loop> """
        """ 522 <statements_loop>	=>	<looping_st>	<statements_loop> """
        """ 523 <statements_loop>	=>	<jump_st>	<statements_loop> """
        """ 524 <statements_loop>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def id_statements_loop(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 525 <id_statements_loop>	=>	id	<id_statements_ext>	<statements_loop> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def conditional_st_loop(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 526 <conditional_st_loop>	=>	<cond_check_loop> """
        """ 527 <conditional_st_loop>	=>	<cond_menu_loop> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def cond_check_loop(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 528 <cond_check_loop>	=>	check	(	<strict_flag_expr>	)	<endb_loop_platter>	<alt_clause_loop>	<instead_clause_loop> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def alt_clause_loop(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 529 <alt_clause_loop>	=>	alt	(	<strict_flag_expr>	)	<endb_loop_platter>	<alt_clause_loop> """
        """ 530 <alt_clause_loop>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def instead_clause_loop(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 531 <instead_clause_loop>	=>	instead	<endb_loop_platter> """
        """ 532 <instead_clause_loop>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def cond_menu_loop(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 533 <cond_menu_loop>	=>	menu	(	<any_expr>	)	<menu_loop_platter> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def menu_loop_platter(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 534 <menu_loop_platter>	=>	{	<choice_clause_loop>	<usual_clause_loop>	} """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def choice_clause_loop(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 535 <choice_clause_loop>	=>	choice	<choice_val>	:	<statements_loop>	<choice_clause_loop> """
        """ 536 <choice_clause_loop>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def usual_clause_loop(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 537 <usual_clause_loop>	=>	usual	:	<statements_loop> """
        """ 538 <usual_clause_loop>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def jump_st(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 539 <jump_st>	=>	<jump_next> """
        """ 540 <jump_st>	=>	<jump_stop> """
        """ 541 <jump_st>	=>	<jump_serve> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def jump_next(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 542 <jump_next>	=>	next	; """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def jump_stop(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 543 <jump_stop>	=>	stop	; """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def jump_serve(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 544 <jump_serve>	=>	serve	<value>	; """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def loop_repeat(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 545 <loop_repeat>	=>	repeat	(	<strict_flag_expr>	)	<endb_loop_platter> """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def loop_order(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 546 <loop_order>	=>	order	<endb_loop_platter>	repeat	(	<strict_flag_expr>	)	; """

        log.info("Exit: " + self.tokens[self.pos].type) # J

    def usual_clause(self):
        log.info("Enter: " + self.tokens[self.pos].type) # J

        """ 547 <usual_clause>	=>	usual	:	<statements_menu> """
        """ 548 <usual_clause>	=>	λ """

        log.info("Exit: " + self.tokens[self.pos].type) # J


if __name__ == "__main__":
    from app.utils.FileHandler import run_file
    
    filepath = "parser.platter"
    code = run_file(filepath)
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    try:
        parser.parse_program()
        print("No Syntax Error")
    except SyntaxError as e:
        print(str(e))
