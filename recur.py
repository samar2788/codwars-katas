def solve(a,b):
    if not (a and b): return [a, b]
    if a >= 2*b: return solve(a%(2*b), b)
    if b >= 2*a: return solve(a, b%(2*a))
    return [a, b]

d = solve(6,19)
print(d)