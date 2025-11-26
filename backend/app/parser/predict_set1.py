PREDICT_SET = {
    "<program>": ["piece", "sip", "flag", "chars", "table", "id", "prepare", "start"],

    "<global_decl>": ["piece", "sip", "flag", "chars"],
    "<global_decl>_1": ["table"],
    "<global_decl>_2": ["id"],
    "<global_decl>_3": ["prepare", "start"],

    "<decl_data_type>": ["piece"],
    "<decl_data_type>_1": ["sip"],
    "<decl_data_type>_2": ["flag"],
    "<decl_data_type>_3": ["chars"],

    "<decl_type>": ["of"],
    "<decl_type>_1": ["["],

    "<ingredient_id>": ["id"],

    "<ingredient_init>": ["="],
    "<ingredient_init>_1": [",,", ";"],

    "<ingredient_id_tail>": [","],
    "<ingredient_id_tail>_1": [";"],

    "<expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],

    "<or_expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],

    "<and_expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],

    "<or_tail>": ["or"],
    "<or_tail>_1": [",,", ";", ")", "]", ":"],

    "<eq_expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],

    "<and_tail>": ["and"],
    "<and_tail>_1": [";"],

    "<rel_expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],

    "<eq_tail>": ["=="],
    "<eq_tail>_1": ["!="],
    "<eq_tail>_2": ["and", ";"],

    "<add_expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],

    "<rel_tail>": [">"],
    "<rel_tail>_1": ["<"],
    "<rel_tail>_2": [">="],
    "<rel_tail>_3": ["<="],
    "<rel_tail>_4": ["==", "!=", "and", ";"],

    "<mult_expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],

    "<add_tail>": ["+"],
    "<add_tail>_1": ["-"],
    "<add_tail>_2": [">", "<", ">=", "<=", "==", "!=", "and", ";"],

    "<unary_expr>": ["not"],
    "<unary_expr>_1": ["(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],

    "<mult_tail>": ["*"],
    "<mult_tail>_1": ["/"],
    "<mult_tail>_2": ["%"],
    "<mult_tail>_3": ["+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";"],

    "<primary_val>": ["("],
    "<primary_val>_1": ["piece_lit"],
    "<primary_val>_2": ["sip_lit"],
    "<primary_val>_3": ["flag_lit"],
    "<primary_val>_4": ["chars_lit"],
    "<primary_val>_5": ["id"],
    "<primary_val>_6": ["append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],

    "<id_tail>": [ "(", "[", ":", "*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";", ",", "]" ],

    "<call_tailopt>": ["("],
    "<call_tailopt>_1": ["[", ":", "*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";", ",", "]"],

    "<accessor_tail>": ["["],
    "<accessor_tail>_1": [":"],
    "<accessor_tail>_2": ["*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";", ",", ")", "]", "=", "+=", "-=", "*=", "/=", "%="],

    "<array_accessor>": ["["],
    "<table_accessor>": [":"],

    "<flavor>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip", "["],
    "<flavor>_1": [")"],

    "<value>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],
    "<value>_1": ["["],

    "<notation_val>": ["piece_lit", "sip_lit", "flag_lit", "chars_lit", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip", "["],
    "<notation_val>_1": ["id"],
    "<notation_val>_2": ["]"],

    "<notation_val1>": ["piece_lit"],
    "<notation_val1>_1": ["sip_lit"],
    "<notation_val1>_2": ["flag_lit"],
    "<notation_val1>_3": ["chars_lit"],
    "<notation_val1>_4": ["append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],
    "<notation_val1>_5": ["["],

    "<element_value_tail>": [","],
    "<element_value_tail>_1": ["]", ","],

    "<notation_val2>": ["id"],
    "<notation_val2>_1": ["piece_lit", "sip_lit", "flag_lit", "chars_lit", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip", "["],

    "<id_notation_tail>": [ "(", "[", ":", "*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";", ",", "]" ],
    "<id_notation_tail>_1": ["="],

    "<assignment_st_eq>": ["="],

    "<field_assignments>": ["id"],
    "<field_assignments>_1": ["]"],

    "<flavor_tail>": [","],
    "<flavor_tail>_1": [")"],

    "<built-in_rec_call>": ["append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],

    "<tail1>": ["("],

    "<built-in_rec>": ["append"],
    "<built-in_rec>_1": ["bill"],
    "<built-in_rec>_2": ["copy"],
    "<built-in_rec>_3": ["cut"],
    "<built-in_rec>_4": ["fact"],
    "<built-in_rec>_5": ["matches"],
    "<built-in_rec>_6": ["pow"],
    "<built-in_rec>_7": ["rand"],
    "<built-in_rec>_8": ["remove"],
    "<built-in_rec>_9": ["reverse"],
    "<built-in_rec>_10": ["search"],
    "<built-in_rec>_11": ["size"],
    "<built-in_rec>_12": ["sort"],
    "<built-in_rec>_13": ["sqrt"],
    "<built-in_rec>_14": ["take"],
    "<built-in_rec>_15": ["tochars"],
    "<built-in_rec>_16": ["topiece"],
    "<built-in_rec>_17": ["tosip"],

    "<call_tail>": ["("],

    "<dimensions>": ["["],
    "<dimensions_tail>": ["["],
    "<dimensions_tail>_1": ["of"],

    "<array_declare>": ["id"],

    "<array_table_init>": ["="],
    "<array_table_init>_1": [",,", ";"],

    "<array_declare_tail>": [","],
    "<array_declare_tail>_1": [";"],

    "<table_prototype>": ["table"],

    "<required_decl>": ["piece", "sip", "flag", "chars", "id"],

    "<decl_head>": ["piece", "sip", "flag", "chars", "id"],

    "<data_types_dims>": ["piece"],
    "<data_types_dims>_1": ["sip"],
    "<data_types_dims>_2": ["flag"],
    "<data_types_dims>_3": ["chars"],
    "<data_types_dims>_4": ["id"],

    "<required_decl_tail>": ["piece", "sip", "flag", "chars", "id"],
    "<required_decl_tail>_1": ["]"],

    "<table_decl>": ["[", "of"],

    "<table_declare>": ["id"],

    "<table_declare_tail>": [","],
    "<table_declare_tail>_1": [";"],

    "<recipe_decl>": ["prepare"],
    "<recipe_decl>_1": ["start"],

    "<spice>": ["piece", "sip", "flag", "chars", "id"],
    "<spice>_1": [")"],

    "<spice_tail>": [","],
    "<spice_tail>_1": [")"],

    "<platter>": ["{"],

    "<local_decl>": ["piece", "sip", "flag", "chars"],
    "<local_decl>_1": ["id"],
    "<local_decl>_2": ["id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip", "check", "menu", "pass", "repeat", "order", "next", "stop", "serve"],

    "<statements>": ["id"],
    "<statements>_1": ["append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],
    "<statements>_2": ["check", "menu"],
    "<statements>_3": ["pass", "repeat", "order"],
    "<statements>_4": ["next", "stop", "serve"],
    "<statements>_5": ["}", "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip", "check", "menu", "pass", "repeat", "order", "next", "stop", "serve", "choice", "usual"],

    "<local_id_tail>": ["of"],
    "<local_id_tail>_1": ["["],
    "<local_id_tail>_2": [":"],
    "<local_id_tail>_3": ["=", "+=", "-=", "*=", "/=", "%="],
    "<local_id_tail>_4": ["("],

    "<]_tail>": ["]"],
    "<]_tail>_1": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip"],

    "<id_statements>": ["id"],

    "<id_statements_ext>": ["("],
    "<id_statements_ext>_1": ["[", ":", "=", "+=", "-=", "*=", "/=", "%="],

    "<assignment_st>": [ "[", ":", "*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=", "and", ";", ",", ")", "]", "=", "+=", "-=", "*=", "/=", "%=" ],

    "<assignment_op>": ["="],
    "<assignment_op>_1": ["+="],
    "<assignment_op>_2": ["-="],
    "<assignment_op>_3": ["*="],
    "<assignment_op>_4": ["/="],
    "<assignment_op>_5": ["%="],

    "<conditional_st>": ["check"],
    "<conditional_st>_1": ["menu"],

    "<cond_check>": ["check"],

    "<alt_clause>": ["alt"],
    "<alt_clause>_1": ["instead", "id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip", "check", "menu", "pass", "repeat", "order", "next", "stop", "serve", "}", "choice", "usual"],

    "<instead_clause>": ["instead"],
    "<instead_clause>_1": ["id", "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand", "remove", "reverse", "search", "size", "sort", "sqrt", "take", "tochars", "topiece", "tosip", "check", "menu", "pass", "repeat", "order", "next", "stop", "serve", "}", "choice", "usual"],

    "<cond_menu>": ["menu"],

    "<menu_platter>": ["{"],

    "<choice_clause>": ["choice"],
    "<choice_clause>_1": ["usual", "}"],

    "<usual_clause>": ["usual"],
    "<usual_clause>_1": ["}"],

    "<looping_st>": ["pass"],
    "<looping_st>_1": ["repeat"],
    "<looping_st>_2": ["order"],

    "<loop_pass>": ["pass"],
    "<loop_repeat>": ["repeat"],
    "<loop_order>": ["order"],

    "<jump_st>": ["next"],
    "<jump_st>_1": ["stop"],
    "<jump_st>_2": ["serve"],

    "<jump_next>": ["next"],
    "<jump_stop>": ["stop"],
    "<jump_serve>": ["serve"]
}
