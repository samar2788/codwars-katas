def count_bits(a):
    b = bin(a).replace('0b', '')
    c = 0
    for i in range(len(b)):
        if b[i] == '1':
            c += 1
    return c
