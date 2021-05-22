from collections import Counter

D = dict(zip("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"))
def last_survivors(s):
    ones, manies = Counter(), Counter()
    for x, y in Counter(s).items():
        (ones, manies)[y > 1][x] += y
    while manies:
        k = next(iter(manies))
        v = manies.pop(k)
        if v % 2:
            if k in ones:
                del ones[k]
                manies[k] = 2
            else:
                ones[k] = 1
        v //= 2
        if D[k] in ones:
            del ones[D[k]]
            v += 1
        (ones, manies)[v > 1][D[k]] += v
    return "".join(ones)


print(last_survivors(
    'zzzab'))
