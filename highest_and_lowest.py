def high_and_low(numbers):
    l=[int(s) for s in numbers.split(' ')]
    l.sort()
    return f"{l[-1]} {l[0]}"


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
print(high_and_low("1 -1"), "1 -1")
print(high_and_low("1 1"), "1 1")
print(high_and_low("-1 -1"), "-1 -1")
print(high_and_low("1 -1 0"), "1 -1")
print(high_and_low("1 1 0"), "1 0")
print(high_and_low("-1 -1 0"), "0 -1")
print(high_and_low("42"), "42 42")
