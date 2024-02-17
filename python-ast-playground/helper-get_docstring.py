"""
This file shows and describe get_docstring method.
"""
import ast

# ast.get_docstring(node, clean=True)
"""
Return the docstring of the given node
(which must be a FunctionDef, AsyncFunctionDef, ClassDef,
or Module node),
"""

code = """
'''
module doc
'''
class MyClass:
    '''
    class doc
    indented doc
    '''
    pass

def add_numbers(a: str, b: str):
    '''
    func doc
    indented doc
    '''
    pass
"""
tree = ast.parse(code)
module_doc = ast.get_docstring(tree)
print(module_doc)  # module doc
print(len(module_doc))  # 10

class_node = tree.body[1]
class_doc = ast.get_docstring(class_node)
print(class_doc)  # class doc\nindented doc
print(len(class_doc))  # 22

func_node = tree.body[2]
func_node = ast.get_docstring(func_node, clean=False)  # clean=False
print(func_node)  # return with whitespaces and offset spaces
print(len(func_node))  # 35
print(ast.dump(tree, indent=4))
