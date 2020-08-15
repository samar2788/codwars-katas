def derive(coefficient, exponent): 
    ce =  int (coefficient * exponent)
    diff = exponent - 1
    return str(ce) + "x^" + str(diff)

d = derive(10, 2)
print(d)