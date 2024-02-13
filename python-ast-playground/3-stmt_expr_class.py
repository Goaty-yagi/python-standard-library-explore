import ast

"""
ast.stmt class serves as a base class for various statement nodes in the AST,
indicating that instances of this class represent statements in Python code.
ast.expr class serves as a base class for various expression nodes in the AST,
indicating that instances of this class represent expression in Python code.
"""

print("stmt is subclass of ast.AST: ", issubclass(ast.stmt, ast.AST))
print("statement class, such as Assign is subclass of stmt: ", issubclass(ast.Assign, ast.stmt)) # stmt is base class

print("expr is subclass of ast.AST: ", issubclass(ast.expr, ast.AST))
print("expression class, such as List is subclass of stmt: ", issubclass(ast.List, ast.expr)) # expr is base class

print("Assign is not subclass of ast.expr: ", issubclass(ast.Assign, ast.expr))

