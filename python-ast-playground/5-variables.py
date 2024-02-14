import ast

"""
class ast.Name(id, ctx) 
ctx will bw 3 types

class ast.Load
- to load the value ex) a
class ast.Store
- to assign the value a = 123
class ast.Del
- to delete the value
"""
content = "123" # ctx will be load
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))

content = "a = 123" # ctx will be store
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))

content = "del a" # ctx will be del
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))

# class ast.Starred(value, ctx)
content = "func(*list)"
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))
