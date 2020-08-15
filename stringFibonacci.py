def solve(n):
    return "0" if n == 0 else "01" if n == 1 else solve(n-1) + solve(n-2)

print(solve(5))

# def solve(n):
#     a,b = '01'
#     print(a)
#     print(b)
#     for _ in range(n): a,b = a+b,a
#     return a

# print(solve(5))