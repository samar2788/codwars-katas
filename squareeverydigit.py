def square_digits(num):
    s = list(str(num))
    l = []
    f = ''
    for i in s:
        l.append(int(i)**2)
    for i in l:
        f += str(i)
    return int(f)
