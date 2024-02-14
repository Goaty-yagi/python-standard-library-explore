"""
Literals is right side of variable. 
"""

import ast

# class ast.Constant(value) represent Constant value(immutable)

content = "1234"
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4)) # value=Constant(value=1234)


# class ast.List(elts, ctx)
# elts contains constant instance include value
content = "[1, 2, 3]"
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))

# class ast.Dict(keys, values)
# keys include Name instance
# vlaues include constant instance
content = "{id: 90, name: 'test'}"
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))


# class ast.JoinedStr(values)
# class ast.FormattedValue(value, conversion, format_spec)
# value from FormattedValue will be Name instance 
# so doesn't include value, but variable name
variable = "test" # This will be FormattedValue
content = 'f"{variable}"' # JoinedStr contains FormattedValue
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))


# format method will be Constant instance
variable = 90
content = "{}".format(variable)
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))
