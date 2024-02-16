"""
This module provides CustomVisitor class inherited from NodeVisitor

About NodeVisitor:
    Methods:
    - visit(node): look for a specific ast.class_name in the node.
    If it is found a method named visit_class_name will be called.
    - generic_visit: go through all child nodes
    - visit_<classname>: Handles the class during the traversal process.
"""

import ast


class CustomVisitor(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print(f"Found function: {node}")
        # self.generic_visit(node)
        # No generic_visit so visit_name won't be called

    def visit_Call(self, node):
        print("Found function call:", node.func.id)
        self.generic_visit(node)  # Name in Call class will be found

    def visit_Name(self, node):
        print("Found function Name:", node.id)
        self.generic_visit(node)

    def visit_Constant(self, node):
        print("Found constant:", node.value)


code = """
def add_numbers(a: str, b: str):
    def test():
        pass
    return a + b
numbers(1,2)
"""

tree = ast.parse(code, type_comments=True)
visitor = CustomVisitor()
visitor.visit(tree)
