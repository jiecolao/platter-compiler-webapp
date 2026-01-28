from app.parser.ast_nodes import *

class ASTReader:
    """Pretty printer for AST nodes"""
    
    def __init__(self, ast_root):
        self.ast_root = ast_root
        self.indent_level = 0
        self.indent_str = "  "
    
    def read(self):
        """Generate a pretty-printed string representation of the AST"""
        if self.ast_root is None:
            return "Empty AST"
        return self._visit(self.ast_root)
    
    def _visit(self, node, prefix=""):
        """Visit a node and generate its string representation"""
        if node is None:
            return f"{prefix}None\n"
        
        result = []
        indent = self.indent_str * self.indent_level
        
        # Handle tuples (used in some node structures)
        if isinstance(node, tuple):
            if len(node) == 2:
                result.append(f"{prefix}({node[0]}, ...)\n")
                self.indent_level += 1
                result.append(self._visit(node[1], self.indent_str * self.indent_level))
                self.indent_level -= 1
            return "".join(result)
        
        if isinstance(node, Program):
            result.append(f"{prefix}Program:\n")
            self.indent_level += 1
            
            if node.global_decl:
                result.append(f"{self.indent_str * self.indent_level}Global Declarations ({len(node.global_decl)}):\n")
                self.indent_level += 1
                for decl in node.global_decl:
                    result.append(self._visit(decl, self.indent_str * self.indent_level))
                self.indent_level -= 1
            
            if node.recipe_decl:
                result.append(f"{self.indent_str * self.indent_level}Recipe Declarations ({len(node.recipe_decl)}):\n")
                self.indent_level += 1
                for recipe in node.recipe_decl:
                    result.append(self._visit(recipe, self.indent_str * self.indent_level))
                self.indent_level -= 1
            
            if node.start_platter:
                result.append(f"{self.indent_str * self.indent_level}Start Platter:\n")
                self.indent_level += 1
                result.append(self._visit(node.start_platter, self.indent_str * self.indent_level))
                self.indent_level -= 1
            
            self.indent_level -= 1
        
        elif isinstance(node, Platter):
            result.append(f"{prefix}Platter:\n")
            self.indent_level += 1
            
            if node.local_decl:
                result.append(f"{self.indent_str * self.indent_level}Local Declarations ({len(node.local_decl)}):\n")
                self.indent_level += 1
                for decl in node.local_decl:
                    result.append(self._visit(decl, self.indent_str * self.indent_level))
                self.indent_level -= 1
            
            if node.statements:
                result.append(f"{self.indent_str * self.indent_level}Statements ({len(node.statements)}):\n")
                self.indent_level += 1
                for stmt in node.statements:
                    result.append(self._visit(stmt, self.indent_str * self.indent_level))
                self.indent_level -= 1
            
            self.indent_level -= 1
        
        elif isinstance(node, IngredientDecl):
            result.append(f"{prefix}IngredientDecl(type={node.data_type}, dims={node.dimensions}):\n")
            if node.id_and_inits:
                self.indent_level += 1
                for id_init in node.id_and_inits:
                    result.append(self._visit(id_init, self.indent_str * self.indent_level))
                self.indent_level -= 1
        
        elif isinstance(node, IdAndInit):
            result.append(f"{prefix}IdAndInit(id={node.identifier}):\n")
            if node.init_value:
                self.indent_level += 1
                result.append(f"{self.indent_str * self.indent_level}Init:\n")
                self.indent_level += 1
                result.append(self._visit(node.init_value, self.indent_str * self.indent_level))
                self.indent_level -= 2
        
        elif isinstance(node, TableDecl):
            result.append(f"{prefix}TableDecl(name={node.table_name}):\n")
            if node.fields:
                self.indent_level += 1
                for field in node.fields:
                    result.append(self._visit(field, self.indent_str * self.indent_level))
                self.indent_level -= 1
        
        elif isinstance(node, RecipeDecl):
            result.append(f"{prefix}RecipeDecl(name={node.recipe_id}, return={node.serve_type}):\n")
            self.indent_level += 1
            if node.spices:
                result.append(f"{self.indent_str * self.indent_level}Parameters ({len(node.spices)}):\n")
                self.indent_level += 1
                for spice in node.spices:
                    result.append(self._visit(spice, self.indent_str * self.indent_level))
                self.indent_level -= 1
            if node.platter:
                result.append(self._visit(node.platter, self.indent_str * self.indent_level))
            self.indent_level -= 1
        
        elif isinstance(node, Spice):
            result.append(f"{prefix}Spice(type={node.data_type}, dims={node.dimensions}, id={node.identifier})\n")
        
        elif isinstance(node, BinaryOp):
            result.append(f"{prefix}BinaryOp(op={node.operator}):\n")
            self.indent_level += 1
            result.append(f"{self.indent_str * self.indent_level}Left:\n")
            self.indent_level += 1
            result.append(self._visit(node.left, self.indent_str * self.indent_level))
            self.indent_level -= 1
            result.append(f"{self.indent_str * self.indent_level}Right:\n")
            self.indent_level += 1
            result.append(self._visit(node.right, self.indent_str * self.indent_level))
            self.indent_level -= 2
        
        elif isinstance(node, UnaryOp):
            result.append(f"{prefix}UnaryOp(op={node.operator}):\n")
            self.indent_level += 1
            result.append(self._visit(node.operand, self.indent_str * self.indent_level))
            self.indent_level -= 1
        
        elif isinstance(node, Literal):
            result.append(f"{prefix}Literal(type={node.literal_type}, value={node.value})\n")
        
        elif isinstance(node, Identifier):
            result.append(f"{prefix}Identifier(name={node.name}):\n")
            if node.indices:
                self.indent_level += 1
                result.append(f"{self.indent_str * self.indent_level}Indices ({len(node.indices)}):\n")
                self.indent_level += 1
                for idx in node.indices:
                    result.append(self._visit(idx, self.indent_str * self.indent_level))
                self.indent_level -= 2
        
        elif isinstance(node, RecipeCall):
            result.append(f"{prefix}RecipeCall(name={node.recipe_name}):\n")
            self.indent_level += 1
            if node.arguments:
                result.append(f"{self.indent_str * self.indent_level}Arguments ({len(node.arguments)}):\n")
                self.indent_level += 1
                for arg in node.arguments:
                    result.append(self._visit(arg, self.indent_str * self.indent_level))
                self.indent_level -= 1
            if node.indices:
                result.append(f"{self.indent_str * self.indent_level}Indices ({len(node.indices)}):\n")
                self.indent_level += 1
                for idx in node.indices:
                    result.append(self._visit(idx, self.indent_str * self.indent_level))
                self.indent_level -= 1
            self.indent_level -= 1
        
        elif isinstance(node, ArrayLiteral):
            result.append(f"{prefix}ArrayLiteral ({len(node.elements)} elements):\n")
            if node.elements:
                self.indent_level += 1
                for elem in node.elements:
                    result.append(self._visit(elem, self.indent_str * self.indent_level))
                self.indent_level -= 1
        
        elif isinstance(node, TableLiteral):
            result.append(f"{prefix}TableLiteral ({len(node.field_assignments)} fields):\n")
            if node.field_assignments:
                self.indent_level += 1
                for field_name, value in node.field_assignments:
                    result.append(f"{self.indent_str * self.indent_level}{field_name}:\n")
                    self.indent_level += 1
                    result.append(self._visit(value, self.indent_str * self.indent_level))
                    self.indent_level -= 1
                self.indent_level -= 1
        
        elif isinstance(node, Assignment):
            result.append(f"{prefix}Assignment(op={node.operator}):\n")
            self.indent_level += 1
            result.append(f"{self.indent_str * self.indent_level}Target:\n")
            self.indent_level += 1
            result.append(self._visit(node.identifier, self.indent_str * self.indent_level))
            self.indent_level -= 1
            result.append(f"{self.indent_str * self.indent_level}Value:\n")
            self.indent_level += 1
            result.append(self._visit(node.value, self.indent_str * self.indent_level))
            self.indent_level -= 2
        
        elif isinstance(node, StandaloneRecipeCall):
            result.append(f"{prefix}StandaloneRecipeCall:\n")
            self.indent_level += 1
            result.append(self._visit(node.recipe_call, self.indent_str * self.indent_level))
            self.indent_level -= 1
        
        elif isinstance(node, CheckStatement):
            result.append(f"{prefix}CheckStatement:\n")
            self.indent_level += 1
            result.append(f"{self.indent_str * self.indent_level}Condition:\n")
            self.indent_level += 1
            result.append(self._visit(node.condition, self.indent_str * self.indent_level))
            self.indent_level -= 1
            result.append(f"{self.indent_str * self.indent_level}Then:\n")
            self.indent_level += 1
            result.append(self._visit(node.then_platter, self.indent_str * self.indent_level))
            self.indent_level -= 1
            if node.alt_clauses:
                for cond, plat in node.alt_clauses:
                    result.append(f"{self.indent_str * self.indent_level}Alt:\n")
                    self.indent_level += 1
                    result.append(f"{self.indent_str * self.indent_level}Condition:\n")
                    self.indent_level += 1
                    result.append(self._visit(cond, self.indent_str * self.indent_level))
                    self.indent_level -= 1
                    result.append(f"{self.indent_str * self.indent_level}Then:\n")
                    self.indent_level += 1
                    result.append(self._visit(plat, self.indent_str * self.indent_level))
                    self.indent_level -= 2
            if node.instead_platter:
                result.append(f"{self.indent_str * self.indent_level}Instead:\n")
                self.indent_level += 1
                result.append(self._visit(node.instead_platter, self.indent_str * self.indent_level))
                self.indent_level -= 1
            self.indent_level -= 1
        
        elif isinstance(node, MenuStatement):
            result.append(f"{prefix}MenuStatement:\n")
            self.indent_level += 1
            result.append(f"{self.indent_str * self.indent_level}Menu Value:\n")
            self.indent_level += 1
            result.append(self._visit(node.menu_value, self.indent_str * self.indent_level))
            self.indent_level -= 1
            if node.choices:
                for choice_val, plat in node.choices:
                    result.append(f"{self.indent_str * self.indent_level}Choice:\n")
                    self.indent_level += 1
                    result.append(self._visit(choice_val, self.indent_str * self.indent_level))
                    result.append(self._visit(plat, self.indent_str * self.indent_level))
                    self.indent_level -= 1
            if node.usual_platter:
                result.append(f"{self.indent_str * self.indent_level}Usual:\n")
                self.indent_level += 1
                result.append(self._visit(node.usual_platter, self.indent_str * self.indent_level))
                self.indent_level -= 1
            self.indent_level -= 1
        
        elif isinstance(node, PassLoop):
            result.append(f"{prefix}PassLoop:\n")
            self.indent_level += 1
            result.append(f"{self.indent_str * self.indent_level}Init:\n")
            self.indent_level += 1
            result.append(self._visit(node.initialization, self.indent_str * self.indent_level))
            self.indent_level -= 1
            result.append(f"{self.indent_str * self.indent_level}Condition:\n")
            self.indent_level += 1
            result.append(self._visit(node.condition, self.indent_str * self.indent_level))
            self.indent_level -= 1
            result.append(f"{self.indent_str * self.indent_level}Update:\n")
            self.indent_level += 1
            result.append(self._visit(node.update, self.indent_str * self.indent_level))
            self.indent_level -= 1
            result.append(f"{self.indent_str * self.indent_level}Body:\n")
            self.indent_level += 1
            result.append(self._visit(node.platter, self.indent_str * self.indent_level))
            self.indent_level -= 2
        
        elif isinstance(node, RepeatLoop):
            result.append(f"{prefix}RepeatLoop:\n")
            self.indent_level += 1
            result.append(f"{self.indent_str * self.indent_level}Condition:\n")
            self.indent_level += 1
            result.append(self._visit(node.condition, self.indent_str * self.indent_level))
            self.indent_level -= 1
            result.append(f"{self.indent_str * self.indent_level}Body:\n")
            self.indent_level += 1
            result.append(self._visit(node.platter, self.indent_str * self.indent_level))
            self.indent_level -= 2
        
        elif isinstance(node, OrderLoop):
            result.append(f"{prefix}OrderLoop:\n")
            self.indent_level += 1
            result.append(f"{self.indent_str * self.indent_level}Body:\n")
            self.indent_level += 1
            result.append(self._visit(node.platter, self.indent_str * self.indent_level))
            self.indent_level -= 1
            result.append(f"{self.indent_str * self.indent_level}Condition:\n")
            self.indent_level += 1
            result.append(self._visit(node.condition, self.indent_str * self.indent_level))
            self.indent_level -= 2
        

        elif isinstance(node, NextStatement):
            result.append(f"{prefix}NextStatement()\n")
        
        elif isinstance(node, StopStatement):
            result.append(f"{prefix}StopStatement()\n")
        
        elif isinstance(node, ServeStatement):
            result.append(f"{prefix}ServeStatement:\n")
            if node.return_value:
                self.indent_level += 1
                result.append(self._visit(node.return_value, self.indent_str * self.indent_level))
                self.indent_level -= 1
        
        elif isinstance(node, ASTNode):
            # Generic ASTNode handling
            result.append(f"{prefix}{node.__repr__()}\n")
        
        else:
            # Fallback for non-ASTNode objects
            result.append(f"{prefix}{repr(node)}\n")
        
        return "".join(result)
    
    def to_dict(self):
        """Convert AST to dictionary format for JSON serialization"""
        if self.ast_root is None:
            return {"type": "Empty", "content": None}
        return self._node_to_dict(self.ast_root)
    
    def _node_to_dict(self, node):
        """Convert a single node to dictionary"""
        if node is None:
            return None
        
        # Handle tuples
        if isinstance(node, tuple):
            if len(node) == 2:
                return {"tuple": [node[0], self._node_to_dict(node[1])]}
            return {"tuple": list(node)}
        
        if isinstance(node, Program):
            return {
                "type": "Program",
                "globalDeclarations": [self._node_to_dict(d) for d in node.global_decl],
                "recipeDeclarations": [self._node_to_dict(r) for r in node.recipe_decl],
                "startPlatter": self._node_to_dict(node.start_platter)
            }
        
        elif isinstance(node, Platter):
            return {
                "type": "Platter",
                "localDeclarations": [self._node_to_dict(d) for d in node.local_decl],
                "statements": [self._node_to_dict(s) for s in node.statements]
            }
        
        elif isinstance(node, IngredientDecl):
            return {
                "type": "IngredientDecl",
                "dataType": node.data_type,
                "dimensions": node.dimensions,
                "declarations": [self._node_to_dict(d) for d in node.id_and_inits]
            }
        
        elif isinstance(node, IdAndInit):
            return {
                "type": "IdAndInit",
                "identifier": node.identifier,
                "initValue": self._node_to_dict(node.init_value)
            }
        
        elif isinstance(node, TableDecl):
            return {
                "type": "TableDecl",
                "tableName": node.table_name,
                "fields": [self._node_to_dict(f) for f in node.fields]
            }
        
        elif isinstance(node, RecipeDecl):
            return {
                "type": "RecipeDecl",
                "recipeId": node.recipe_id,
                "serveType": node.serve_type,
                "spices": [self._node_to_dict(s) for s in node.spices],
                "platter": self._node_to_dict(node.platter)
            }
        
        elif isinstance(node, Spice):
            return {
                "type": "Spice",
                "dataType": node.data_type,
                "dimensions": node.dimensions,
                "identifier": node.identifier
            }
        
        elif isinstance(node, BinaryOp):
            return {
                "type": "BinaryOp",
                "operator": node.operator,
                "left": self._node_to_dict(node.left),
                "right": self._node_to_dict(node.right)
            }
        
        elif isinstance(node, UnaryOp):
            return {
                "type": "UnaryOp",
                "operator": node.operator,
                "operand": self._node_to_dict(node.operand)
            }
        
        elif isinstance(node, Literal):
            return {
                "type": "Literal",
                "literalType": node.literal_type,
                "value": node.value
            }
        
        elif isinstance(node, Identifier):
            return {
                "type": "Identifier",
                "name": node.name,
                "indices": [self._node_to_dict(i) for i in node.indices]
            }
        
        elif isinstance(node, RecipeCall):
            return {
                "type": "RecipeCall",
                "recipeName": node.recipe_name,
                "arguments": [self._node_to_dict(a) for a in node.arguments],
                "indices": [self._node_to_dict(i) for i in node.indices]
            }
        
        elif isinstance(node, ArrayLiteral):
            return {
                "type": "ArrayLiteral",
                "elements": [self._node_to_dict(e) for e in node.elements]
            }
        
        elif isinstance(node, TableLiteral):
            return {
                "type": "TableLiteral",
                "fields": {name: self._node_to_dict(val) for name, val in node.field_assignments}
            }
        
        elif isinstance(node, Assignment):
            return {
                "type": "Assignment",
                "identifier": self._node_to_dict(node.identifier),
                "operator": node.operator,
                "value": self._node_to_dict(node.value)
            }
        
        elif isinstance(node, StandaloneRecipeCall):
            return {
                "type": "StandaloneRecipeCall",
                "recipeCall": self._node_to_dict(node.recipe_call)
            }
        
        elif isinstance(node, CheckStatement):
            return {
                "type": "CheckStatement",
                "condition": self._node_to_dict(node.condition),
                "thenPlatter": self._node_to_dict(node.then_platter),
                "altClauses": [
                    {"condition": self._node_to_dict(c), "platter": self._node_to_dict(p)}
                    for c, p in node.alt_clauses
                ],
                "insteadPlatter": self._node_to_dict(node.instead_platter)
            }
        
        elif isinstance(node, MenuStatement):
            return {
                "type": "MenuStatement",
                "menuValue": self._node_to_dict(node.menu_value),
                "choices": [
                    {"choiceValue": self._node_to_dict(v), "platter": self._node_to_dict(p)}
                    for v, p in node.choices
                ],
                "usualPlatter": self._node_to_dict(node.usual_platter)
            }
        
        elif isinstance(node, PassLoop):
            return {
                "type": "PassLoop",
                "initialization": self._node_to_dict(node.initialization),
                "condition": self._node_to_dict(node.condition),
                "update": self._node_to_dict(node.update),
                "platter": self._node_to_dict(node.platter)
            }
        
        elif isinstance(node, RepeatLoop):
            return {
                "type": "RepeatLoop",
                "condition": self._node_to_dict(node.condition),
                "platter": self._node_to_dict(node.platter)
            }
        
        elif isinstance(node, OrderLoop):
            return {
                "type": "OrderLoop",
                "platter": self._node_to_dict(node.platter),
                "condition": self._node_to_dict(node.condition)
            }
        

        elif isinstance(node, NextStatement):
            return {"type": "NextStatement"}
        
        elif isinstance(node, StopStatement):
            return {"type": "StopStatement"}
        
        elif isinstance(node, ServeStatement):
            return {
                "type": "ServeStatement",
                "returnValue": self._node_to_dict(node.return_value)
            }
        
        elif isinstance(node, ASTNode):
            return {
                "type": node.node_type,
                "representation": repr(node)
            }
        
        else:
            return {"type": "Unknown", "value": str(node)}


def pretty_print_ast(ast_root):
    """Convenience function to pretty print an AST"""
    reader = ASTReader(ast_root)
    return reader.read()


def ast_to_dict(ast_root):
    """Convenience function to convert AST to dictionary"""
    reader = ASTReader(ast_root)
    return reader.to_dict()
