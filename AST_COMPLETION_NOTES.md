# Complete AST Integration for Platter Parser
# All updates needed to finish AST building

This file documents all remaining parser methods that need AST integration.
See INTEGRATION_PLAN.md for details.

The user wants ALL methods completed, not incremental testing, because stubs break the parser.
Need to complete:
- Recipe parsing (serve_type, spice, decl_head, primitive_types_dims)
- Local declarations (local_decl, local_id_tail)
- Statements (statements, id_statements, assignment_st)  
- Conditionals (conditional_st, check/menu structures)
- Loops (looping_st, pass/repeat/order structures)
- Jumps (jump_st, serve/next/stop)

All must return proper AST nodes while maintaining original parser flow.
