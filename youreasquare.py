import math


def is_square(n):
    if n < 0:
        return False
    else:
        sr = math.sqrt(n)
        if (sr - math.floor(sr)) == 0:
            return True
        else:
            return False
