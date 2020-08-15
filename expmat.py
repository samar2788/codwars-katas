def expression_matter(a, b, c):
    return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))


d = expression_matter(9, 7, 2)
print(d)
