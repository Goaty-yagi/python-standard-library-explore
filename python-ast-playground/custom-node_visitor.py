import ast
"""
This module provides CustomNodeVisitor class
inherited from NodeVisitor class
"""


class CustomNodeVisitor(ast.NodeVisitor):
    """
    Custom AST NodeVisitor class for counting occurrences of specific nodes.

    Attributes:
    - sum: Total count of nodes visited.
    - node_count: Dictionary to store counts of different node types.
    """

    def __init__(self) -> None:
        """
        Initializes the CustomNodeVisitor object.
        """
        self.sum = 0
        self.node_count = {}

    def visit(self, node: ast.AST, *args) -> dict[str: int] | None:
        """
        Visits the given AST node and returns counts for a specified subset of keys, if provided.

        Parameters:
        - node: AST node to visit.
        - *args: Subset of keys to count.

        Returns:
        - None if no subset keys provided, or a dictionary containing counts for the specified subset keys.
        """
        super().visit(node)
        return self.get_counts_subset(*args) if len(args) else None

    def generic_visit(self, node: ast.AST) -> None:
        """
        A generic visit method that increments the node count and continues the traversal.

        Parameters:
        - node: AST node to visit.
        """
        self.sum += 1
        super().generic_visit(node)

    def get_counts_subset(self, *key_list: list[str]) -> dict[str: int]:
        """
        Returns a dictionary containing counts for the specified subset of keys.

        Parameters:
        - *key_list: Subset of keys to count.

        Returns:
        - Dictionary with counts for the specified keys.
        """
        temp_dict = dict()
        for key in key_list:
            if key in self.node_count.keys():
                temp_dict[key] = self.node_count[key]
        return temp_dict

    # *** visit_classname methods from here ***

    def visit_Call(self, node: ast.AST) -> None:
        """
        Visits a Call node and counts method or function calls.

        Parameters:
        - node: Call node in the AST.
        """
        if isinstance(node.func, ast.Attribute):
            # Handling calls to the method.
            self.node_count[node.func.attr] = self.node_count.get(
                node.func.attr, 0) + 1
        elif isinstance(node.func, ast.Name):
            # Assuming simple function calls.
            function_name = node.func.id
            self.node_count[function_name] = self.node_count.get(
                function_name, 0) + 1
        self.generic_visit(node)

    def visit_For(self, node):
        """
        Visits a For node and counts occurrences.

        Parameters:
        - node: For node in the AST.
        """
        self.node_count["for"] = self.node_count.get(
            "for", 0) + 1
        self.generic_visit(node)

    def visit_While(self, node):
        """
        Visits a While node and counts occurrences.

        Parameters:
        - node: While node in the AST.
        """
        self.node_count["while"] = self.node_count.get(
            "while", 0) + 1
        self.generic_visit(node)

    def visit_Import(self, node):
        """
        Visits an Import node and counts occurrences.

        Parameters:
        - node: Import node in the AST.
        """
        self.node_count["import"] = self.node_count.get(
            "import", 0) + 1
        self.generic_visit(node)


code = """
import ast

def add_numbers(a: str, b: str):
    def test():
        pass
    return a + b
numbers(1,2)
print("{}, {}".format(a, b))
while(True):
    a.method(te)
"""

tree = ast.parse(code, type_comments=True)
visitor = CustomNodeVisitor()
print(visitor.visit(tree))
print(visitor.node_count)
print(visitor.sum)
print(visitor.get_counts_subset('while', 'import', 'loop'))
