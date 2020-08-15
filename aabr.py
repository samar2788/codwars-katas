def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

d = abbrevName("evan cole")
print(d)