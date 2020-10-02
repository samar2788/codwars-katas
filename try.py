def basic_op(operator, value1, value2):
    b=str(value1)+operator+str(value2)
    return int(eval(b))

print(basic_op('+', 4, 7))
print(basic_op('-', 15, 18))
print(basic_op('*', 5, 5))
print(basic_op('/', 49, 7))
