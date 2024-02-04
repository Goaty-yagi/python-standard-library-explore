import ast  # module
from abc import ABC

""" ast.AST is not representing a node. """

# AST is also not concrete class. You can call it Base class.
print("AST is not abstract class: ", isinstance(ast.AST, ABC))

# Each concrete class has an attribute _fields which
# gives the names of all child nodes.
# AST does not represent a specific node with child nodes.
print(ast.AST._fields)
