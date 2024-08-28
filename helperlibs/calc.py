import sympy

# inp = "123+124+1233-41241*51+4124+5/6+(32132/(541234+4214*3123)/523-31)"

inp = "32*50-14+5"

ex = sympy.parsing.sympy_parser.parse_expr(inp)

print(ex)













# print(inp)

# if "(" in inp:

#     if ")" not in inp:
#         raise "ERROR NON CLOSED PARANTHESIS"
#     else:
#         pass

#     first_parenthesisleft = inp.index("(")
#     last_parenthesisright = len(inp)- inp[::-1].index(")")

#     print(first_parenthesisleft, last_parenthesisright)
#     paranthesis_part = inp[first_parenthesisleft:last_parenthesisright]

# print(paranthesis_part)