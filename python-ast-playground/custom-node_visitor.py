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
    - attr_reset: Boolean to check if attributes need to reset. 
    - last_node: Last node of the initial node.
    - node_count: Dictionary to store counts of different node types.
    - format_values: List to store format value to check specifiers.
    """

    def __init__(self) -> None:
        """
        Initializes the CustomNodeVisitor object.
        """
        self.sum = 0
        self.attr_reset = False
        self.last_node = None
        self.node_count = {}
        self.format_values = []

    def visit(self, node: ast.AST, *args) -> dict[str: int] | None:
        """
        Visits the given AST node and returns counts for a specified subset of keys, if provided.

        Parameters:
        - node: AST node to visit.
        - *args: Subset of keys to count.

        Returns:
        - None if no subset keys provided, or a dictionary containing counts for the specified subset keys.
        """
        if self.attr_reset:
            self.reset_attributes()
        if self.last_node is None:
            self.set_last_node(node)

        super().visit(node)

        if self.last_node is node:
            self.attr_reset = True
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

    def format_specifier_check(self, specifier: str = "", node: ast.AST = {},):
        """
        Checks if a specific format specifier is present in any of the format values.

        Parameters:
        - node: AST node being processed.
        - specifier: Format specifier to check.

        Returns:
        - True if the specifier is present in any format value, False otherwise.
        """
        if specifier == '':
            raise ValueError("specifier argument is missing.")
        if node:
            self.visit(node)
        if len(self.format_values):
            return any(specifier in val for val in self.format_values)

    def set_last_node(self, node) -> None:
        """
        Sets the last_node attribute to the last child node of the given AST node's body.

        Parameters:
        - node: AST node to determine the last child node.
        """

        # Assume that the visitation process starts with the visit method.
        self.last_node = list(ast.iter_child_nodes(node.body[-1]))[-1]

    def reset_attributes(self) -> None:
        """
        Resets all attributes of the CustomNodeVisitor instance to their default values.
        """
        for key in vars(self):
            setattr(self, key, CustomNodeVisitor().__getattribute__(key))

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
            if node.func.attr == 'format':
                self.format_values.append(node.func.value.value)
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
print("{}, ko {%d}".format(a, b))
while(True):
    a.method(te)
"""

tree = ast.parse(code, type_comments=True)
visitor = CustomNodeVisitor()
print(ast.dump(tree, indent=4))
print(visitor.visit(tree, ''))
print(visitor.node_count)
print(visitor.sum)
print(visitor.get_counts_subset('while', 'import', 'loop'))
print(visitor.format_specifier_check("mo", node=tree))
