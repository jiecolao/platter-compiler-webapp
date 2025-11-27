FOLLOW_SET = {
    "<program>": [],
    "<global_decl>": ["prepare", "start"],
    "<decl_data_type>": [
        "piece", "sip", "flag", "chars", "table", "id",
        "prepare", "start", "append", "bill", "copy", "cut",
        "fact", "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "check", "menu", "pass", "repeat",
        "order", "next", "stop", "serve"
    ],
    "<decl_type>": [
        "piece", "sip", "flag", "chars", "table", "id",
        "prepare", "start", "append", "bill", "copy", "cut",
        "fact", "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "check", "menu", "pass", "repeat",
        "order", "next", "stop", "serve"
    ],
    "<ingredient_id>": [";"],
    "<ingredient_init>": [",", ";"],
    "<ingredient_id_tail>": [";"],
    "<expr>": [",", ";", ")", "]", ":"],
    "<or_expr>": [",", ";", ")", "]", ":"],
    "<and_expr>": ["or", ",", ";", ")", "]", ":"],
    "<or_tail>": [",", ";", ")", "]", ":"],
    "<eq_expr>": ["and", ";"],
    "<and_tail>": [";"],
    "<rel_expr>": ["==", "!=", "and", ";"],
    "<eq_tail>": ["and", ";"],
    "<add_expr>": [">", "<", ">=", "<=", "==", "!=", "and", ";"],
    "<rel_tail>": ["==", "!=", "and", ";"],
    "<mult_expr>": ["+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";"],
    "<add_tail>": ["+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";"],
    "<unary_expr>": ["*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";"],
    "<mult_tail>": ["*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";"],
    "<primary_val>": ["*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";"],
    "<id_tail>": ["*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";", ",", "]"],
    "<call_tailopt>": ["[", ":", "*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";", ",", "]"],
    "<accessor_tail>": [
        "*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and",
        ";", ",", ")", "]", "=", "+=", "-=", "*=", "/=", "%=",
        "id", "append", "bill", "copy", "cut", "fact", "matches",
        "pow", "rand", "remove", "reverse", "search", "size", "sort",
        "sqrt", "take", "tochars", "topiece", "tosip", "check",
        "menu", "pass", "repeat", "order", "next", "stop", "serve"
    ],
    "<array_accessor>": [
        "*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and",
        ";", ",", ")", "]", "=", "+=", "-=", "*=", "/=", "%=",
        "id", "append", "bill", "copy", "cut", "fact", "matches",
        "pow", "rand", "remove", "reverse", "search", "size",
        "sort", "sqrt", "take", "tochars", "topiece", "tosip",
        "check", "menu", "pass", "repeat", "order", "next",
        "stop", "serve"
    ],
    "<table_accessor>": [
        "*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and",
        ";", "id", "append", "bill", "copy", "cut", "fact", "matches",
        "pow", "rand", "remove", "reverse", "search", "size",
        "sort", "sqrt", "take", "tochars", "topiece", "tosip",
        "check", "menu", "pass", "repeat", "order", "next",
        "stop", "serve", ",", ")", "]", "=", "+=", "-=", "*=", "/=", "%="
    ],
    "<flavor>": [")"],
    "<value>": [",", ")", ";"],
    "<notation_val>": ["]"],
    "<element_value_tail>": ["]"],
    "<notation_val1>": [",", "]"],
    "<id_notation_tail>": ["]"],
    "<assignment_st_eq>": ["id", "]"],
    "<field_assignments>": ["]"],
    "<flavor_tail>": [")"],
    "<built-in_rec_call>": ["*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";", ",", "]"],
    "<tail1>": ["*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";", ",", "]"],
    "<built-in_rec>": ["("],
    "<call_tail>": ["[", ":", "*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";", ",", "]"],
    "<dimensions>": ["of"],
    "<dimensions_tail>": ["of"],
    "<array_declare>": [";"],
    "<array_table_init>": [",", ";"],
    "<array_declare_tail>": [";"],
    "<table_prototype>": [
        "piece", "sip", "flag", "chars", "table", "id", "prepare", "start"
    ],
    "<required_decl>": ["]"],
    "<decl_head>": [";", "(", ",", ")"],
    "<data_types_dims>": ["of"],
    "<required_decl_tail>": ["]"],
    "<table_decl>": [
        "piece", "sip", "flag", "chars", "table", "id", "prepare", "start"
    ],
    "<table_declare>": [";"],
    "<table_declare_tail>": [";"],
    "<recipe_decl>": ["start"],
    "<spice>": [")"],
    "<spice_tail>": [")"],
    "<platter>": [
        "prepare", "start", "alt", "instead",
        "id", "append", "bill", "copy", "cut", "fact", "matches",
        "pow", "rand", "remove", "reverse", "search", "size",
        "sort", "sqrt", "take", "tochars", "topiece", "tosip",
        "check", "menu", "pass", "repeat", "order", "next",
        "stop", "serve", "choice", "usual"
    ],
    "<local_decl>": [
        "id", "append", "bill", "copy", "cut", "fact", "matches",
        "pow", "rand", "remove", "reverse", "search", "size",
        "sort", "sqrt", "take", "tochars", "topiece", "tosip",
        "check", "menu", "pass", "repeat", "order", "next",
        "stop", "serve"
    ],
    "<statements>": [
        "}", "id", "append", "bill", "copy", "cut", "fact", "matches",
        "pow", "rand", "remove", "reverse", "search", "size",
        "sort", "sqrt", "take", "tochars", "topiece", "tosip",
        "check", "menu", "pass", "repeat", "order", "next",
        "stop", "serve", "choice", "usual"
    ],
    "<local_id_tail>": [
        "id", "append", "bill", "copy", "cut", "fact", "matches",
        "pow", "rand", "remove", "reverse", "search", "size",
        "sort", "sqrt", "take", "tochars", "topiece", "tosip",
        "check", "menu", "pass", "repeat", "order", "next",
        "stop", "serve"
    ],
    "<]_tail>": [
        "id", "append", "bill", "copy", "cut", "fact", "matches",
        "pow", "rand", "remove", "reverse", "search", "size",
        "sort", "sqrt", "take", "tochars", "topiece", "tosip",
        "check", "menu", "pass", "repeat", "order", "next",
        "stop", "serve"
    ],
    "<id_statements>": [
        "id", "append", "bill", "copy", "cut", "fact", "matches",
        "pow", "rand", "remove", "reverse", "search", "size",
        "sort", "sqrt", "take", "tochars", "topiece", "tosip",
        "check", "menu", "pass", "repeat", "order", "next",
        "stop", "serve", "choice", "usual"
    ],
    "<id_statements_ext>": [
        "id", "append", "bill", "copy", "cut", "fact", "matches",
        "pow", "rand", "remove", "reverse", "search", "size",
        "sort", "sqrt", "take", "tochars", "topiece", "tosip",
        "check", "menu", "pass", "repeat", "order", "next",
        "stop", "serve", "choice", "usual"
    ],
    "<assignment_st>": [
        ";", "not", "(", "piece_lit", "sip_lit", "flag_lit",
        "chars_lit", "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse", "search",
        "size", "sort", "sqrt", "take", "tochars", "topiece",
        "tosip"
    ],
    "<assignment_op>": [
        "not", "(", "piece_lit", "sip_lit", "flag_lit",
        "chars_lit", "id", "append", "bill", "copy", "cut",
        "fact", "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "["
    ],
    "<conditional_st>": [
        "id", "append", "bill", "copy", "cut", "fact", "matches",
        "pow", "rand", "remove", "reverse", "search", "size",
        "sort", "sqrt", "take", "tochars", "topiece", "tosip",
        "check", "menu", "pass", "repeat", "order", "next",
        "stop", "serve", "choice", "usual"
    ],
    "<cond_check>": [
        "id", "append", "bill", "copy", "cut", "fact", "matches",
        "pow", "rand", "remove", "reverse", "search", "size",
        "sort", "sqrt", "take", "tochars", "topiece", "tosip",
        "check", "menu", "pass", "repeat", "order", "next",
        "stop", "serve", "choice", "usual"
    ],
    "<alt_clause>": [
        "instead", "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse", "search",
        "size", "sort", "sqrt", "take", "tochars", "topiece",
        "tosip", "check", "menu", "pass", "repeat", "order",
        "next", "stop", "serve", "choice", "usual"
    ],
    "<instead_clause>": [
        "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "check", "menu", "pass", "repeat",
        "order", "next", "stop", "serve", "choice", "usual"
    ],
    "<cond_menu>": [
        "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "check", "menu", "pass", "repeat",
        "order", "next", "stop", "serve", "choice", "usual"
    ],
    "<menu_platter>": [
        "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "check", "menu", "pass", "repeat",
        "order", "next", "stop", "serve", "choice", "usual"
    ],
    "<choice_clause>": ["usual"],
    "<usual_clause>": [],
    "<looping_st>": [
        "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "check", "menu", "pass",
        "repeat", "order", "next", "stop", "serve",
        "choice", "usual"
    ],
    "<loop_pass>": [
        "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "check", "menu", "pass",
        "repeat", "order", "next", "stop", "serve",
        "choice", "usual"
    ],
    "<loop_repeat>": [
        "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "check", "menu", "pass",
        "repeat", "order", "next", "stop", "serve",
        "choice", "usual"
    ],
    "<loop_order>": [
        "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "check", "menu", "pass",
        "repeat", "order", "next", "stop", "serve",
        "choice", "usual"
    ],
    "<jump_st>": [
        "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "check", "menu", "pass",
        "repeat", "order", "next", "stop", "serve",
        "choice", "usual"
    ],
    "<jump_next>": [
        "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "check", "menu", "pass",
        "repeat", "order", "next", "stop", "serve",
        "choice", "usual"
    ],
    "<jump_stop>": [
        "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "check", "menu", "pass",
        "repeat", "order", "next", "stop", "serve",
        "choice", "usual"
    ],
    "<jump_serve>": [
        "id", "append", "bill", "copy", "cut", "fact",
        "matches", "pow", "rand", "remove", "reverse",
        "search", "size", "sort", "sqrt", "take", "tochars",
        "topiece", "tosip", "check", "menu", "pass",
        "repeat", "order", "next", "stop", "serve",
        "choice", "usual"
    ]
}
