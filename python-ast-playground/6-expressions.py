"""
This file shows and describe Expr class and some subclasses.

Contents:
- class ast.Expr(value):
- class ast.UnaryOp(op, operand)
- class ast.BinOp(left, op, right)
- class ast.BoolOp(op, values)
- class ast.Compare(left, ops, comparators)
- class ast.Call(func, args, keywords)
"""
import ast

# class ast.Expr(value)
"""
class ast.Expr(value)
When an expression, such as a function call, 
appears as a statement by itself with its 
return value not used or stored, it is wrapped
in this container. value holds one of the other
nodes, such as
- Constant
- Name
- Lambda
- Yield
- YieldFrom
"""
content = """def fun():
    return 'test'""" # doesn't have Expr instance
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))


content = """def fun():
    print(123)""" # This have Expr instance because print is called
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))

""" 
class ast.UnaryOp(op, operand)
op: will be one of these class below.
operand: will be the operand(constant or name most of the time)
class ast.UAdd
- +6
class ast.USub
- -5
class ast.Not
- not 5
class ast.Invert
x = 5
~5
"""

# UAdd
content = "+5"
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))
x = 1
print(~x)

# USub
content = "-5"
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))
x = 1
print(~x)

# Not
content = "not 5"
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))

# Invert
content = "~v"
parsed_ast =  ast.parse(content)
print(ast.dump(parsed_ast, indent=4))


# class ast.BinOp(left, op, right)
"""
left: is left operand
op: is operation class down below
right: is right operand
class ast.Add: 2 + 2
class ast.Sub: 2 - 1
class ast.Mult: 2 * 3
class ast.Div: 3 / 3
class ast.FloorDiv: 7 // 2
class ast.Mod: 90 % 10
class ast.Pow: 2 ** 2
class ast.LShift: 5 << 2
class ast.RShift: 5 >> 2
class ast.BitOr: 5 | 3
class ast.BitXor: 5 ^ 3
class ast.BitAnd: 5 & 3
class ast.MatMult: @ (new op?)
Binary operator tokens.
"""

content = "2 + 8" 
parsed_ast =  ast.parse(content) # op will be Add
print(ast.dump(parsed_ast, indent=4))

# class ast.BoolOp(op, values)
"""
Consecutive operations with the same operator, such as a or b or c,
are collapsed into one node with several values.
op: is operation class down below
values: will have values to be compared with the op.

class ast.And
class ast.Or
Boolean operator tokens.
"""

content = "9 or 10" 
parsed_ast =  ast.parse(content) 
# op will be Or
# values contains Constant instances 
print(ast.dump(parsed_ast, indent=4))


# class ast.Compare(left, ops, comparators)
"""
left: will be the left value
ops: will contains operation classes down below
comparators: will contains the other values to be compared

class ast.Eq: ==
class ast.NotEq: !=
class ast.Lt: <
class ast.LtE: <=
class ast.Gt: >
class ast.GtE: >=
class ast.Is: is
class ast.IsNot: is not
class ast.In: in 
class ast.NotIn: not in
"""

content = "0 > 10 <= 15" 
parsed_ast =  ast.parse(content)
# left will be 0
# ops will be Gt and LtE
# comparators will be 10 and 15
print(ast.dump(parsed_ast, indent=4))

# class ast.Call(func, args, keywords)