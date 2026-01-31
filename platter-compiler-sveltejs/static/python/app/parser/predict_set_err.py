# repeated non terminals are merged in this list for error catching

PREDICT_SET_ERR = {
    "<program>": [
        "piece", "sip", "flag", "chars", "table", "id", "prepare", "start"
    ],

    "<global_decl>": [
        "piece", "sip", "flag", "chars", "table", "id", "prepare", "start"
    ],

    "<decl_data_type>": [
        "piece", "sip", "flag", "chars"
    ],

    "<decl_type>": [
        "of", "["
    ],

    "<ingredient_id>": ["id"],

    "<ingredient_init>": [
        "=", ",", ";"
    ],

    "<ingredient_id_tail>": [
        ",", ";"
    ],

    "<expr>": [
        "not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip"
    ],

    "<or_expr>": [
        "not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip"
    ],

    "<and_expr>": [
        "not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip"
    ],

    "<or_tail>": [
        "or", ",", ";", ")", "]"
    ],

    "<eq_expr>": [
        "not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip"
    ],

    "<and_tail>": [
        "and", "or", ",", ";", ")", "]"
    ],

    "<rel_expr>": [
        "not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip"
    ],

    "<eq_tail>": [
        "==", "!=", "and", "or", ",", ";", ")", "]"
    ],

    "<add_expr>": [
        "not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip"
    ],

    "<rel_tail>": [
        ">", "<", ">=", "<=", "==", "!=", "and", "or", ",", ";", ")", "]"
    ],

    "<mult_expr>": [
        "not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip"
    ],

    "<add_tail>": [
        "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", "or", ",", ";", ")", "]"
    ],

    "<unary_expr>": [
        "not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip"
    ],

    "<mult_tail>": [
        "*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and",
        "or", ",", ";", ")", "]"
    ],

    "<primary_val>": [
        "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip"
    ],

    "<id_tail>": [
        "(", "[", ":", "*", "/", "%", "+", "-", ">", "<", ">=", "<=",
        "==", "!=", "and", "or", ",", ";", ")", "]"
    ],

    "<call_tailopt>": [
        "(", "[", ":", "*", "/", "%", "+", "-", ">", "<", ">=", "<=",
        "==", "!=", "and", "or", ",", ";", ")", "]"
    ],

    "<accessor_tail>": [
        "[", ":", "*", "/", "%", "+", "-", ">", "<", ">=", "<=",
        "==", "!=", "and", "or", ",", ";", ")", "=", "+=", "-=", "*=", "/=", "%=", "]"
    ],

    "<array_accessor>": ["["],
    "<table_accessor>": [":"],

    "<flavor>": [
        "not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip", "[", ")"
    ],

    "<value>": [
        "not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip", "["
    ],

    "<notation_val>": [
        "piece_lit", "sip_lit", "flag_lit", "chars_lit", "[", "id", "]"
    ],

    "<array_element>": [
        "piece_lit", "sip_lit", "flag_lit", "chars_lit", "["
    ],

    "<element_value_tail>": [
        ",", "]"
    ],

    "<array_element_id>": [
        "id", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "["
    ],

    "<array_or_table>": [
        ",", "=", "]"
    ],

    "<field_assignments>": [
        "id", "]"
    ],

    "<flavor_tail>": [
        ",", ")"
    ],

    "<built-in_rec_call>": [
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip"
    ],

    "<tail1>": ["("],

    "<built-in_rec>": [
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip"
    ],

    "<call_tail>": ["("],

    "<dimensions>": ["["],

    "<dimensions_tail>": ["[", "of"],

    "<array_declare>": ["id"],

    "<array_table_init>": ["=", ",", ";"],

    "<array_declare_tail>": [",", ";"],

    "<table_prototype>": ["table"],

    "<required_decl>": ["piece", "sip", "flag", "chars", "id"],

    "<decl_head>": ["piece", "sip", "flag", "chars", "id"],

    "<primitive_types_dims>": ["piece", "sip", "flag", "chars", "id"],

    "<required_decl_tail>": ["piece", "sip", "flag", "chars", "id", "]"],

    "<table_decl>": ["[", "of"],

    "<table_declare>": ["id"],

    "<table_declare_tail>": [",", ";"],

    "<recipe_decl>": ["prepare", "start"],

    "<serve_type>": ["piece", "sip", "flag", "chars", "id"],

    "<spice>": ["piece", "sip", "flag", "chars", "id", ")"],

    "<spice_tail>": [",", ")"],

    "<platter>": ["{"],

    "<local_decl>": [
        "piece", "sip", "flag", "chars", "id",
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip", "check", "menu", "pass", "repeat",
        "order", "next", "stop", "serve", "}"
    ],

    "<statements>": [
        "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip", "check", "menu", "pass", "repeat",
        "order", "next", "stop", "serve", "}", "choice", "usual"
    ],

    "<local_id_tail>": [
        "of", "[", ":", "=", "+=", "-=", "*=", "/=", "%=", "("
    ],

    "<]_tail>": [
        "]", "not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
        "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
        "remove", "reverse", "search", "size", "sort", "sqrt", "take",
        "tochars", "topiece", "tosip"
    ],

    "<id_statements>": ["id"],

    "<id_statements_ext>": [
        "(", "[", ":", "=", "+=", "-=", "*=", "/=", "%="
    ],

    "<assignment_st>": [
        "[", ":", "*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==",
        "!=", "and", "or", ",", ";", ")", "=", "+=", "-=", "*=", "/=", "%=", "]"
    ],

    "<assignment_op>": [
        "=", "+=", "-=", "*=", "/=", "%="
    ],

    "<conditional_st>": ["check", "menu"],

    "<cond_check>": ["check"],

    "<alt_clause>": [
        "alt", "instead", "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse", "search", "size",
        "sort", "sqrt", "take", "tochars", "topiece", "tosip", "check",
        "menu", "pass", "repeat", "order", "next", "stop", "serve", "}",
        "choice", "usual"
    ],

    "<instead_clause>": [
        "instead", "id", "append", "bill", "copy", "cut", "fact", "matches",
        "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt",
        "take", "tochars", "topiece", "tosip", "check", "menu", "pass",
        "repeat", "order", "next", "stop", "serve", "}", "choice", "usual"
    ],

    "<cond_menu>": ["menu"],

    "<menu_platter>": ["{"],

    "<choice_clause>": ["choice", "usual", "}"],

    "<choice_val>": ["piece_lit", "chars_lit"],

    "<usual_clause>": ["usual", "}"],

    "<looping_st>": ["pass", "repeat", "order"],

    "<loop_pass>": ["pass"],

    "<initialization>": ["id"],

    "<update>": ["id"],

    "<loop_repeat>": ["repeat"],

    "<loop_order>": ["order"],

    "<jump_st>": ["next", "stop", "serve"],

    "<jump_next>": ["next"],

    "<jump_stop>": ["stop"],

    "<jump_serve>": ["serve"]
}
