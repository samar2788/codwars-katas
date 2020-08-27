from functools import lru_cache


@lru_cache(maxsize=1000)
def solve(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '01'
    elif n == 2:
        return '010'
    else:
        return solve(n-1) + solve(n-2)
