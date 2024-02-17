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
        self.__sum = 0
        self.__attr_reset = False
        self.__last_node = None
        self.node_count = {}
        self.__format_values = []

    @property
    def sum(self) -> int:
        """
        Property method to get the value of the 'sum' attribute.

        Returns:
        - The total count of nodes visited.
        """
        return self.__sum

    @sum.setter
    def sum(self, value: any):
        """
        Setter method for 'sum' attribute, raise Attribute error.

        Parameters:
        - value(any): The value to set (ignored).

        Raises:
        - AttributeError: This attribute is read-only.
        """
        raise AttributeError(CustomNodeVisitor._read_only_error_text("sum"))

    @property
    def attr_reset(self) -> None:
        """
        Property method to raise ValueError for "attr_reset" attribute.

        Raises:
        - ValueError: Not allowed to access.
        """
        raise ValueError(
            CustomNodeVisitor._not_allowed_error_text("attr_reset"))

    @attr_reset.setter
    def attr_reset(self, value: any) -> None:
        """
        Setter method to raise ValueError for "attr_reset" attribute.

        Parameters:
        - value(any): The value to set (ignored).

        Raises:
        - ValueError: Not allowed to access.
        """
        raise ValueError(
            CustomNodeVisitor._not_allowed_error_text("attr_reset"))

    @property
    def last_node(self) -> None:
        """
        Property method to raise ValueError for "last_node" attribute.

        Raises:
        - ValueError: Not allowed to access.
        """
        raise ValueError(
            CustomNodeVisitor._not_allowed_error_text("last_node"))

    @last_node.setter
    def last_node(self, value: any) -> None:
        """
        Property method to raise ValueError for "last_node" attribute.

        Parameters:
        - value: The value to set (ignored).

        Raises:
        - ValueError: Not allowed to access.
        """
        raise ValueError(
            CustomNodeVisitor._not_allowed_error_text("last_node"))

    @property
    def format_values(self) -> None:
        """
        Property method to raise ValueError for "format_values" attribute.

        Raises:
        - ValueError: Not allowed to access.
        """
        raise ValueError(
            CustomNodeVisitor._not_allowed_error_text("format_values"))

    @format_values.setter
    def format_values(self, value: any) -> None:
        """
        Property method to raise ValueError for "format_values" attribute.

        Parameters:
        - value(any): The value to set (ignored).

        Raises:
        - ValueError: Not allowed to access.
        """
        raise ValueError(
            CustomNodeVisitor._not_allowed_error_text("format_values"))

    @staticmethod
    def _not_allowed_error_text(attr: str) -> str:
        """
        Static method to provide error text for not allowed attribute access.

        Parameters:
        - attr(str): The attribute name.

        Returns:
        - Error message string.
        """
        return f"You are not allowed to access '{attr}' attribute."

    @staticmethod
    def _read_only_error_text(attr: str) -> str:
        """
        Staticmethod to provide error text for read_only.

        Parameters:
        - attr(str): The attribute name.

        Return:
        - Error message string.
        """
        return f"Attribute '{attr}' is read-only."

    def visit(self, node: ast.AST, *args) -> dict[str: int] | None:
        """
        Visits the given AST node and returns counts for
        a specified subset of keys, if provided.

        Parameters:
        - node: AST node to visit.
        - *args: Subset of keys to count.

        Returns:
        - None if no subset keys provided, or a dictionary
        containing counts for the specified subset keys.
        """
        if self.__attr_reset:
            self.reset_attributes()
        if self.__last_node is None:
            self.set_last_node(node)

        super().visit(node)

        if self.__last_node is node:
            self.__attr_reset = True
        return self.get_counts_subset(*args) if len(args) else None

    def generic_visit(self, node: ast.AST) -> None:
        """
        A generic visit method that increments
        the node count and continues the traversal.

        Parameters:
        - node: AST node to visit.
        """
        self.__sum += 1
        super().generic_visit(node)

    def get_counts_subset(self, *key_list: list[str]) -> dict[str: int]:
        """
        Returns a dictionary containing counts for
        the specified subset of keys.

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
        Checks if a specific format specifier is present
        in any of the format values.

        Parameters:
        - node: AST node being processed.
        - specifier: Format specifier to check.

        Returns:
        - True if the specifier is present in any format value,
        False otherwise.
        """
        if specifier == '':
            raise ValueError("specifier argument is missing.")
        if node:
            self.visit(node)
        if len(self.__format_values):
            return any(specifier in val for val in self.__format_values)

    def set_last_node(self, node) -> None:
        """
        Sets the last_node attribute to the last child node
        of the given AST node's body.

        Parameters:
        - node: AST node to determine the last child node.
        """

        # Assume that the visitation process starts with the visit method.
        self.__last_node = list(ast.iter_child_nodes(node.body[-1]))[-1]

    def reset_attributes(self) -> None:
        """
        Resets all attributes of the CustomNodeVisitor
        instance to their default values.
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
                self.__format_values.append(node.func.value.value)
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

    def visit_Try(self, node):
        """
        Visits an Import node and counts occurrences.

        Parameters:
        - node: Import node in the AST.
        """
        self.node_count["try"] = self.node_count.get(
            "try", 0) + 1
        self.generic_visit(node)

    def visit_Return(self, node):
        """
        Visits an Import node and counts occurrences.

        Parameters:
        - node: Import node in the AST.
        """
        self.node_count["return"] = self.node_count.get(
            "return", 0) + 1
        self.generic_visit(node)

    def visit_Assign(self, node):
        """
        Visits an Assign node and counts occurrences.

        Parameters:
        - node: Assign node in the AST.
        """
        self.node_count["assign"] = self.node_count.get(
            "assign", 0) + 1
        self.generic_visit(node)

    def visit_AnnAssign(self, node):
        """
        Visits an AnnAssign node and counts occurrences.

        Parameters:
        - node: AnnAssign node in the AST.
        """
        self.node_count["ann_assign"] = self.node_count.get(
            "ann_assign", 0) + 1
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        """
        Visits an AugAssign node and counts occurrences.

        Parameters:
        - node: AugAssign node in the AST.
        """
        self.node_count["aug_assign"] = self.node_count.get(
            "aug_assign", 0) + 1
        self.generic_visit(node)


code = """
import ast
'''
return
'''
def add_numbers(a: str, b: str):
    def test():
        a = b
        a += 1
        a:int = b
    return a + b
numbers(1,2)
print("{}, ko {%d}".format(a, b))
while(True):
    a.method(te)
    try:
        pass
    except:
        pass
"""

tree = ast.parse(code, type_comments=True)
visitor = CustomNodeVisitor()
print(ast.dump(tree, indent=4))
print(visitor.visit(tree, ''))
print(visitor.node_count)
print(visitor.sum)
print(visitor.get_counts_subset('while', 'import', 'loop'))
print(visitor.format_specifier_check("mo", node=tree))
