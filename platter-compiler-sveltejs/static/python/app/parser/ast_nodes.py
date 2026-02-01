# Base node
class ASTNode:
    def __init__(self, node_type="ASTNode"): 
        self.node_type = node_type
    
    def __repr__(self):
        return f"{self.__class__.__name__}()"

class Program(ASTNode):
    """Root node of the AST"""
    def __init__(self): 
        super().__init__("Program")
        self.global_decl = []  # List of IngredientDecl, ArrayDecl, or TableDecl nodes
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

class GlobalDecl(ASTNode):
    """Variable declaration node"""
    def __init__(self, data_type=None, dimensions=0, id_and_inits=None):
        super().__init__("IngredientDecl")
        self.scope = "global"
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