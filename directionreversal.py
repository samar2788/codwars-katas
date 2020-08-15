def solve(a):
    stod = []
    dtos = []
    c = 0
    s = ''
    fl = []
    for i in a:
        stod.append(i.split()[0])
    dtos = list(reversed(stod))
    dtosl = len(dtos)
    for i in range(dtosl):
        if dtos[i] == 'Left':
            dtos[i] = 'Right'
        elif dtos[i] == 'Right':
            dtos[i] = 'Left'
        elif dtos[i] == 'Begin':
            break
    dtos = dtos[-1:]+dtos[:-1]
    b = list(reversed(a))
    for i in b:
        i = ' '.join(i.split()[1:])
        s = dtos[c] + " "+i
        c += 1
        fl.append(s)
    return fl
