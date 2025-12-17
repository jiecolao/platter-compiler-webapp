PREDICT_SET = {
    "<program>": ["piece", "sip", "flag", "chars", "table", "id", "λ"],

    "<global_decl>": ["piece", "sip", "flag", "chars"],
    "<global_decl_1>": ["table"],
    "<global_decl_2>": ["id"],
    "<global_decl_3>": ["prepare", "start"],

    "<decl_data_type>": ["piece"],
    "<decl_data_type_1>": ["sip"],
    "<decl_data_type_2>": ["flag"],
    "<decl_data_type_3>": ["chars"],

    "<decl_type>": ["of"],
    "<decl_type_1>": ["["],

    "<ingredient_id>": ["id"],

    "<ingredient_init>": ["="],
    "<ingredient_init_1>": [",,", ";"],

    "<ingredient_id_tail>": [","],
    "<ingredient_id_tail_1>": [";"],

    "<expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
               "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
               "remove", "reverse", "search", "size", "sort", "sqrt", "take",
               "tochars", "topiece", "tosip"],

    "<or_expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
                  "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
                  "remove", "reverse", "search", "size", "sort", "sqrt", "take",
                  "tochars", "topiece", "tosip"],

    "<and_expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
                   "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
                   "remove", "reverse", "search", "size", "sort", "sqrt", "take",
                   "tochars", "topiece", "tosip"],

    "<or_tail>": ["or"],
    "<or_tail_1>": [",,", ";", ")", "]"],

    "<eq_expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
                  "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
                  "remove", "reverse", "search", "size", "sort", "sqrt", "take",
                  "tochars", "topiece", "tosip"],

    "<and_tail>": ["and"],
    "<and_tail_1>": ["or", ",,", ";", ")", "]"],

    "<rel_expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
                   "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
                   "remove", "reverse", "search", "size", "sort", "sqrt", "take",
                   "tochars", "topiece", "tosip"],

    "<eq_tail>": ["=="],
    "<eq_tail_1>": ["!="],
    "<eq_tail_2>": ["and", "or", ",,", ";", ")", "]"],

    "<add_expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
                   "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
                   "remove", "reverse", "search", "size", "sort", "sqrt", "take",
                   "tochars", "topiece", "tosip"],

    "<rel_tail>": [">"],
    "<rel_tail_1>": ["<"],
    "<rel_tail_2>": [">="],
    "<rel_tail_3>": ["<="],
    "<rel_tail_4>": ["==", "!=", "and", "or", ",,", ";", ")", "]"],

    "<mult_expr>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
                    "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
                    "remove", "reverse", "search", "size", "sort", "sqrt", "take",
                    "tochars", "topiece", "tosip"],

    "<add_tail>": ["+"],
    "<add_tail_1>": ["-"],
    "<add_tail_2>": [">", "<", ">=", "<=", "==", "!=", "and", "or", ",,", ";", ")", "]"],

    "<unary_expr>": ["not"],
    "<unary_expr_1>": ["(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
                       "append", "bill", "copy", "cut", "fact", "matches", "pow",
                       "rand", "remove", "reverse", "search", "size", "sort",
                       "sqrt", "take", "tochars", "topiece", "tosip"],

    "<mult_tail>": ["*"],
    "<mult_tail_1>": ["/"],
    "<mult_tail_2>": ["%"],
    "<mult_tail_3>": ["+", "-", ">", "<", ">=", "<=", "==", "!=", "and", "or", ",,", ";", ")", "]"],

    "<primary_val>": ["("],
    "<primary_val_1>": ["piece_lit"],
    "<primary_val_2>": ["sip_lit"],
    "<primary_val_3>": ["flag_lit"],
    "<primary_val_4>": ["chars_lit"],
    "<primary_val_5>": ["id"],
    "<primary_val_6>": ["append", "bill", "copy", "cut", "fact", "matches", "pow",
                        "rand", "remove", "reverse", "search", "size", "sort",
                        "sqrt", "take", "tochars", "topiece", "tosip"],

    "<id_tail>": ["(", "λ"],

    "<call_tailopt>": ["("],
    "<call_tailopt_1>": ["[", ":", "*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==",
                         "!=", "and", "or", ",,", ";", ")", "]"],

    "<accessor_tail>": ["["],
    "<accessor_tail_1>": [":"],
    "<accessor_tail_2>": ["*", "/", "%", "+", "-", ">", "<", ">=", "<=", "==", "!=",
                          "and", "or", ",,", ";", ")", "=", "+=", "-=", "*=", "/=", "%=", "]"],

    "<array_accessor>": ["["],
    "<table_accessor>": [":"],

    "<flavor>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
                 "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
                 "remove", "reverse", "search", "size", "sort", "sqrt", "take",
                 "tochars", "topiece", "tosip", "["],
    "<flavor_1>": [")"],

    "<value>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
                "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
                "remove", "reverse", "search", "size", "sort", "sqrt", "take",
                "tochars", "topiece", "tosip"],
    "<value_1>": ["["],

    "<notation_val>": ["piece_lit", "sip_lit", "flag_lit", "chars_lit", "["],
    "<notation_val_1>": ["id"],
    "<notation_val_2>": ["]"],

    "<array_element>": ["piece_lit"],
    "<array_element_1>": ["sip_lit"],
    "<array_element_2>": ["flag_lit"],
    "<array_element_3>": ["chars_lit"],
    "<array_element_4>": ["["],

    "<field_assignments>": ["id"],
    "<field_assignments_1>": ["]"],

    "<element_value_tail>": [","],
    "<element_value_tail_1>": ["]"],

    "<flavor_tail>": [","],
    "<flavor_tail_1>": [")"],

    "<built-in_rec_call>": ["append", "bill", "copy", "cut", "fact", "matches", "pow",
                            "rand", "remove", "reverse", "search", "size", "sort",
                            "sqrt", "take", "tochars", "topiece", "tosip"],

    "<tail1>": ["("],

    "<built-in_rec>": ["append"],
    "<built-in_rec_1>": ["bill"],
    "<built-in_rec_2>": ["copy"],
    "<built-in_rec_3>": ["cut"],
    "<built-in_rec_4>": ["fact"],
    "<built-in_rec_5>": ["matches"],
    "<built-in_rec_6>": ["pow"],
    "<built-in_rec_7>": ["rand"],
    "<built-in_rec_8>": ["remove"],
    "<built-in_rec_9>": ["reverse"],
    "<built-in_rec_10>": ["search"],
    "<built-in_rec_11>": ["size"],
    "<built-in_rec_12>": ["sort"],
    "<built-in_rec_13>": ["sqrt"],
    "<built-in_rec_14>": ["take"],
    "<built-in_rec_15>": ["tochars"],
    "<built-in_rec_16>": ["topiece"],
    "<built-in_rec_17>": ["tosip"],

    "<call_tail>": ["("],

    "<dimensions>": ["["],
    "<dimensions_tail>": ["["],
    "<dimensions_tail_1>": ["of"],

    "<array_declare>": ["id"],

    "<array_table_init>": ["="],
    "<array_table_init_1>": [",,", ";"],

    "<array_declare_tail>": [","],
    "<array_declare_tail_1>": [";"],

    "<table_prototype>": ["table"],

    "<required_decl>": ["piece", "sip", "flag", "chars", "id"],
    "<decl_head>": ["piece", "sip", "flag", "chars", "id"],

    "<primitive_types_dims>": ["piece"],
    "<primitive_types_dims_1>": ["sip"],
    "<primitive_types_dims_2>": ["flag"],
    "<primitive_types_dims_3>": ["chars"],
    "<primitive_types_dims_4>": ["id"],

    "<required_decl_tail>": ["piece", "sip", "flag", "chars", "id"],
    "<required_decl_tail_1>": ["]"],

    "<table_decl>": ["[", "λ"],

    "<table_declare>": ["id"],

    "<table_declare_tail>": [","],
    "<table_declare_tail_1>": [";"],

    "<recipe_decl>": ["prepare"],
    "<recipe_decl_1>": ["start"],

    "<serve_type>": ["piece", "sip", "flag", "chars", "id"],

    "<spice>": ["piece", "sip", "flag", "chars", "id"],
    "<spice_1>": [")"],

    "<spice_tail>": [","],
    "<spice_tail_1>": [")"],

    "<platter>": ["{"],

    "<local_decl>": ["piece", "sip", "flag", "chars"],
    "<local_decl_1>": ["id"],
    "<local_decl_2>": ["id", "append", "bill", "copy", "cut", "fact", "matches", "pow",
                       "rand", "remove", "reverse", "search", "size", "sort", "sqrt",
                       "take", "tochars", "topiece", "tosip", "check", "menu", "pass",
                       "repeat", "order", "next", "stop", "serve", "}"],

    "<statements>": ["id"],
    "<statements_1>": ["append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
                       "remove", "reverse", "search", "size", "sort", "sqrt", "take",
                       "tochars", "topiece", "tosip"],
    "<statements_2>": ["check", "menu"],
    "<statements_3>": ["pass", "repeat", "order"],
    "<statements_4>": ["next", "stop", "serve"],
    "<statements_5>": ["}", "id", "append", "bill", "copy", "cut", "fact", "matches",
                       "pow", "rand", "remove", "reverse", "search", "size", "sort",
                       "sqrt", "take", "tochars", "topiece", "tosip", "check", "menu",
                       "pass", "repeat", "order", "next", "stop", "serve",
                       "choice", "usual"],

    "<local_id_tail>": ["of"],
    "<local_id_tail_1>": ["["],
    "<local_id_tail_2>": [":"],
    "<local_id_tail_3>": ["=", "+=", "-=", "*=", "/=", "%="],
    "<local_id_tail_4>": ["("],

    "<]_tail>": ["]"],
    "<]_tail_1>": ["not", "(", "piece_lit", "sip_lit", "flag_lit", "chars_lit", "id",
                   "append", "bill", "copy", "cut", "fact", "matches", "pow", "rand",
                   "remove", "reverse", "search", "size", "sort", "sqrt", "take",
                   "tochars", "topiece", "tosip"],

    "<id_statements>": ["id"],

    "<id_statements_ext>": ["("],
    "<id_statements_ext_1>": ["[", ":", "=", "+=", "-=", "*=", "/=", "%="],

    "<assignment_st>": ["[", ":", "λ"],

    "<assignment_op>": ["="],
    "<assignment_op_1>": ["+="],
    "<assignment_op_2>": ["-="],
    "<assignment_op_3>": ["*="],
    "<assignment_op_4>": ["/="],
    "<assignment_op_5>": ["%="],

    "<conditional_st>": ["check"],
    "<conditional_st_1>": ["menu"],

    "<cond_check>": ["check"],

    "<alt_clause>": ["alt"],
    "<alt_clause_1>": ["instead", "id", "append", "bill", "copy", "cut", "fact",
                       "matches", "pow", "rand", "remove", "reverse", "search",
                       "size", "sort", "sqrt", "take", "tochars", "topiece",
                       "tosip", "check", "menu", "pass", "repeat", "order",
                       "next", "stop", "serve", "}", "choice", "usual"],

    "<instead_clause>": ["instead"],
    "<instead_clause_1>": ["id", "append", "bill", "copy", "cut", "fact", "matches",
                           "pow", "rand", "remove", "reverse", "search", "size",
                           "sort", "sqrt", "take", "tochars", "topiece", "tosip",
                           "check", "menu", "pass", "repeat", "order", "next",
                           "stop", "serve", "}", "choice", "usual"],

    "<cond_menu>": ["menu"],

    "<menu_platter>": ["{"],

    "<choice_clause>": ["choice"],
    "<choice_clause_1>": ["usual", "}"],

    "<choice_val>": ["piece_lit"],
    "<choice_val_1>": ["chars_lit"],

    "<usual_clause>": ["usual"],
    "<usual_clause_1>": ["}"],

    "<looping_st>": ["pass"],
    "<looping_st_1>": ["repeat"],
    "<looping_st_2>": ["order"],

    "<loop_pass>": ["pass"],

    "<initialization>": ["id"],
    "<update>": ["id"],

    "<loop_repeat>": ["repeat"],
    "<loop_order>": ["order"],

    "<jump_st>": ["next"],
    "<jump_st_1>": ["stop"],
    "<jump_st_2>": ["serve"],

    "<jump_next>": ["next"],
    "<jump_stop>": ["stop"],
    "<jump_serve>": ["serve"],
}
