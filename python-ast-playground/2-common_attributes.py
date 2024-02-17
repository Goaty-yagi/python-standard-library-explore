import ast

"""
Instances of ast.expr and ast.stmt subclasses have
1, lineno,
2, col_offset,
3, end_lineno,
4, end_col_offset
attributes.
"""

code = """

for i in range(5):
    print("{:d}".format(i))
"""

parsed_ast = ast.parse(code)  # This is Module instance
instance = parsed_ast.body[0]
print("This instance is from For class: ", isinstance(instance, ast.For))
print("For instance is subclass of stmt class:", issubclass(ast.For, ast.stmt))
print("        lineno: ", instance.lineno) # returns 3, for loop start in the line number 3
print("    end_lineno: ", instance.end_lineno) # returns 4, for loop block end in the line number 4
print("    col_offset: ", instance.col_offset) # returns 0, for loop start at 0 offset in line 3
print("end_col_offset: ", instance.end_col_offset) # returns 25, for loop end at 25 offset in the line number 4
print("       _fields:", instance._fields) # doesn't include print attribute as default.

print(ast.dump(parsed_ast, indent=4))
