def solution(a):
    c = 0
    for i in range(1, a):
        if i % 3 == 0 and i % 5 != 0:
            c += i
        elif i % 3 != 0 and i % 5 == 0:
            c += i
        elif i % 3 == 0 and i % 5 == 0:
            c += i
    return c
