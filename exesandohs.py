def xo(a):
    cx = 0
    co = 0
    for i in range(len(a)):
        if a[i].lower() == 'x':
            cx += 1
        elif a[i].lower() == 'o':
            co += 1

    if cx == co:
        return True
    elif cx == co == 0:
        return True
    else:
        return False
