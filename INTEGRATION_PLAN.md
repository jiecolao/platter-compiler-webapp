# AST Integration Completion Plan

## Critical Fixes Needed

### 1. RecipeDecl Constructor Fix
Currently calling: `RecipeDecl(recipe_name, params, return_type, body)`
Should be: `RecipeDecl(return_type, recipe_name, params, body)`

### 2. serve_type() - Must parse and return Spice/type info
### 3. spice() - Must parse parameters and return list of Spice nodes
### 4. decl_head() - Must parse and return Spice node
### 5. primitive_types_dims() - Must return (type, dimensions) tuple

### 6. local_decl(platter_node) - Must add IngredientDecl nodes to platter
### 7. statements(platter_node) - Must add statement nodes to platter

### 8. id_statements() - Return Assignment or StandaloneRecipeCall
### 9. assignment_st() - Return Assignment node

### 10. conditional_st() - Return CheckStatement or MenuStatement
### 11. looping_st() - Return PassLoop, RepeatLoop, or OrderLoop
### 12. jump_st() - Return ServeStatement, NextStatement, or StopStatement

## All methods must integrate AST building without breaking the original parser logic.
