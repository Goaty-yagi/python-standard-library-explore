"""
Literals is right side of variable. 
"""

import ast

# class ast.Constant(value) represent Constant value(immutable)

content = "1234"
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4)) # value=Constant(value=1234)


content = "[1, 2, 3]"
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))