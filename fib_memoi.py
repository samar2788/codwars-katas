from functools import lru_cache

@lru_cache(maxsize=1000)
def solve(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n > 2:
        return solve(n-1) + solve(n-2)

print(solve(5))