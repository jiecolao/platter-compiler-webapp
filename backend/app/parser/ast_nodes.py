# Base node
class ASTNode:
    def __init__(self, node_type="ASTNode"): 
        self.node_type = node_type
    
    def __repr__(self):
        return f"{self.__class__.__name__}()"


# ============================================================================
# PROGRAM STRUCTURE
# ============================================================================

class Program(ASTNode):
    """Root node of the AST"""
    def __init__(self): 
        super().__init__("Program")
        self.global_decl = []  # List of IngredientDecl or TableDecl nodes
        self.recipe_decl = []  # List of RecipeDecl nodes
        self.start_platter = None  # Platter node
    
    def add_global_decl(self, node): 
        self.global_decl.append(node)
        
    def add_recipe_decl(self, node): 
        self.recipe_decl.append(node)

    def set_start_platter(self, node): 
        self.start_platter = node
    
    def __repr__(self):
        return f"Program(global_decl={len(self.global_decl)}, recipe_decl={len(self.recipe_decl)}, start_platter={'Yes' if self.start_platter else 'No'})" 


class Platter(ASTNode):
    """Represents a code block with local declarations and statements"""
    def __init__(self):
        super().__init__("Platter")
        self.local_decl = []  # List of IngredientDecl nodes
        self.statements = []  # List of statement nodes
    
    def add_local_decl(self, node):
        self.local_decl.append(node)
    
    def add_statement(self, node):
        self.statements.append(node)
    
    def __repr__(self):
        return f"Platter(local_decl={len(self.local_decl)}, statements={len(self.statements)})" 


# ============================================================================
# DECLARATIONS
# ============================================================================

class IngredientDecl(ASTNode):
    """Variable declaration node"""
    def __init__(self, data_type, dimensions=0, id_and_inits=None):
        super().__init__("IngredientDecl")
        self.data_type = data_type  # "piece", "sip", "flag", "chars"
        self.dimensions = dimensions  # 0 for scalar, 1+ for arrays
        self.id_and_inits = id_and_inits or []  # List of IdAndInit nodes
    
    def add_id_and_init(self, node): 
        self.id_and_inits.append(node)
    
    def __repr__(self):
        return f"IngredientDecl(type={self.data_type}, dims={self.dimensions}, vars={len(self.id_and_inits)})"


class IdAndInit(ASTNode):
    """Identifier with optional initialization"""
    def __init__(self, identifier, init_value=None):
        super().__init__("IdAndInit")
        self.identifier = identifier  # String
        self.init_value = init_value  # Value node or None
    
    def __repr__(self):
        return f"IdAndInit(id={self.identifier}, init={'Yes' if self.init_value else 'No'})"


class TableDecl(ASTNode):
    """Table (struct) declaration"""
    def __init__(self, table_name, fields=None):
        super().__init__("TableDecl")
        self.table_name = table_name  # String
        self.fields = fields or []  # List of IngredientDecl nodes
    
    def add_field(self, node):
        self.fields.append(node)
    
    def __repr__(self):
        return f"TableDecl(name={self.table_name}, fields={len(self.fields)})"


class RecipeDecl(ASTNode):
    """Function declaration"""
    def __init__(self, serve_type, recipe_id, spices=None, platter=None):
        super().__init__("RecipeDecl")
        self.serve_type = serve_type  # Return type: "piece", "sip", "flag", "chars", or None for void
        self.recipe_id = recipe_id  # String (function name)
        self.spices = spices or []  # List of Spice (parameter) nodes
        self.platter = platter  # Platter node (function body)
    
    def add_spice(self, node):
        self.spices.append(node)
    
    def set_platter(self, node):
        self.platter = node
    
    def __repr__(self):
        return f"RecipeDecl(name={self.recipe_id}, return={self.serve_type}, params={len(self.spices)})"


class Spice(ASTNode):
    """Function parameter"""
    def __init__(self, data_type, dimensions, identifier):
        super().__init__("Spice")
        self.data_type = data_type  # "piece", "sip", "flag", "chars"
        self.dimensions = dimensions  # 0 for scalar, 1+ for arrays
        self.identifier = identifier  # String
    
    def __repr__(self):
        return f"Spice(type={self.data_type}, dims={self.dimensions}, id={self.identifier})"


# ============================================================================
# EXPRESSIONS / VALUES
# ============================================================================

class BinaryOp(ASTNode):
    """Binary operation node"""
    def __init__(self, operator, left, right):
        super().__init__("BinaryOp")
        self.operator = operator  # String: "+", "-", "*", "/", "%", "||", "&&", "==", "!=", "<", ">", "<=", ">="
        self.left = left  # Value node
        self.right = right  # Value node
    
    def __repr__(self):
        return f"BinaryOp(op={self.operator})"


class UnaryOp(ASTNode):
    """Unary operation node"""
    def __init__(self, operator, operand):
        super().__init__("UnaryOp")
        self.operator = operator  # String: "!", "-"
        self.operand = operand  # Value node
    
    def __repr__(self):
        return f"UnaryOp(op={self.operator})"


class Literal(ASTNode):
    """Literal value (number, string, boolean)"""
    def __init__(self, literal_type, value):
        super().__init__("Literal")
        self.literal_type = literal_type  # "int_lit", "float_lit", "str_lit", "flag_true", "flag_false"
        self.value = value  # Actual value
    
    def __repr__(self):
        return f"Literal(type={self.literal_type}, value={self.value})"


class Identifier(ASTNode):
    """Variable reference with optional array/table accessors"""
    def __init__(self, name, indices=None):
        super().__init__("Identifier")
        self.name = name  # String
        self.indices = indices or []  # List of Value nodes (for array/table access)
    
    def add_index(self, index_node):
        self.indices.append(index_node)
    
    def __repr__(self):
        return f"Identifier(name={self.name}, indices={len(self.indices)})"


class RecipeCall(ASTNode):
    """Function call with optional array/table accessors"""
    def __init__(self, recipe_name, arguments=None, indices=None):
        super().__init__("RecipeCall")
        self.recipe_name = recipe_name  # String (function name)
        self.arguments = arguments or []  # List of Value nodes (arguments/flavors)
        self.indices = indices or []  # List of Value nodes (for when function returns array/table)
    
    def add_argument(self, arg_node):
        self.arguments.append(arg_node)
    
    def add_index(self, index_node):
        self.indices.append(index_node)
    
    def __repr__(self):
        return f"RecipeCall(name={self.recipe_name}, args={len(self.arguments)}, indices={len(self.indices)})"


class ArrayLiteral(ASTNode):
    """Array literal [1, 2, 3]"""
    def __init__(self, elements=None):
        super().__init__("ArrayLiteral")
        self.elements = elements or []  # List of Value nodes
    
    def add_element(self, element_node):
        self.elements.append(element_node)
    
    def __repr__(self):
        return f"ArrayLiteral(elements={len(self.elements)})"


class TableLiteral(ASTNode):
    """Table literal {x: 1, y: 2}"""
    def __init__(self, field_assignments=None):
        super().__init__("TableLiteral")
        self.field_assignments = field_assignments or []  # List of (field_name: str, value: Value) tuples
    
    def add_field(self, field_name, value_node):
        self.field_assignments.append((field_name, value_node))
    
    def __repr__(self):
        return f"TableLiteral(fields={len(self.field_assignments)})"


# ============================================================================
# STATEMENTS
# ============================================================================

class Assignment(ASTNode):
    """Assignment statement"""
    def __init__(self, identifier, operator, value):
        super().__init__("Assignment")
        self.identifier = identifier  # Identifier node (can have indices)
        self.operator = operator  # String: "=", "+=", "-=", "*=", "/=", "%="
        self.value = value  # Value node
    
    def __repr__(self):
        return f"Assignment(op={self.operator})"


class StandaloneRecipeCall(ASTNode):
    """Standalone function call statement"""
    def __init__(self, recipe_call):
        super().__init__("StandaloneRecipeCall")
        self.recipe_call = recipe_call  # RecipeCall node
    
    def __repr__(self):
        return f"StandaloneRecipeCall()"


class CheckStatement(ASTNode):
    """Check statement (check-alt-instead)"""
    def __init__(self, condition, then_platter, alt_clauses=None, instead_platter=None):
        super().__init__("CheckStatement")
        self.condition = condition  # Value node
        self.then_platter = then_platter  # Platter node
        self.alt_clauses = alt_clauses or []  # List of (condition, platter) tuples for 'alt'
        self.instead_platter = instead_platter  # Platter node or None for 'instead'
    
    def add_alt(self, condition, platter):
        self.alt_clauses.append((condition, platter))
    
    def set_instead(self, platter):
        self.instead_platter = platter
    
    def __repr__(self):
        return f"CheckStatement(alts={len(self.alt_clauses)}, instead={'Yes' if self.instead_platter else 'No'})"


class MenuStatement(ASTNode):
    """Menu statement (menu-choice-usual)"""
    def __init__(self, menu_value, choices=None, usual_platter=None):
        super().__init__("MenuStatement")
        self.menu_value = menu_value  # Value node
        self.choices = choices or []  # List of (choice_value, platter) tuples for 'choice'
        self.usual_platter = usual_platter  # Platter node or None for 'usual'
    
    def add_choice(self, choice_value, platter):
        self.choices.append((choice_value, platter))
    
    def set_usual(self, platter):
        self.usual_platter = platter
    
    def __repr__(self):
        return f"MenuStatement(choices={len(self.choices)}, usual={'Yes' if self.usual_platter else 'No'})"


class PassLoop(ASTNode):
    """Pass loop (for loop)"""
    def __init__(self, initialization, condition, update, platter):
        super().__init__("PassLoop")
        self.initialization = initialization  # Assignment node
        self.condition = condition  # Value node
        self.update = update  # Assignment node
        self.platter = platter  # Platter node
    
    def __repr__(self):
        return f"PassLoop()"


class RepeatLoop(ASTNode):
    """Repeat loop (while loop)"""
    def __init__(self, condition, platter):
        super().__init__("RepeatLoop")
        self.condition = condition  # Value node
        self.platter = platter  # Platter node
    
    def __repr__(self):
        return f"RepeatLoop()"


class OrderLoop(ASTNode):
    """Order loop (do-while loop)"""
    def __init__(self, platter, condition):
        super().__init__("OrderLoop")
        self.platter = platter  # Platter node
        self.condition = condition  # Value node
    
    def __repr__(self):
        return f"OrderLoop()"


class NextStatement(ASTNode):
    """Continue/next statement"""
    def __init__(self):
        super().__init__("NextStatement")
    
    def __repr__(self):
        return "NextStatement()"


class StopStatement(ASTNode):
    """Break/stop statement"""
    def __init__(self):
        super().__init__("StopStatement")
    
    def __repr__(self):
        return "StopStatement()"


class ServeStatement(ASTNode):
    """Return/serve statement"""
    def __init__(self, return_value=None):
        super().__init__("ServeStatement")
        self.return_value = return_value  # Value node or None (for void return)
    
    def __repr__(self):
        return f"ServeStatement(has_value={'Yes' if self.return_value else 'No'})"