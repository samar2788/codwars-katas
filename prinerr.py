def printer_error(s):
    c = 0
    al = str(len(s))
    for i in s:
        if i not in "abcdefghijklm":
            c += 1
    nc = str(c)
    return (nc + "/" +al)