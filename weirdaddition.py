def add(num1, num2):
    sl = []
    fs = ''
    if len(str(num1)) == len(str(num2)):
        ln1 = [int(i) for i in str(num1)]
        ln2 = [int(i) for i in str(num2)]
        for i in range(len(ln1)):
            sum = ln1[i]+ln2[i]
            sl.append(sum)
        for i in sl:
            fs += str(i)
        return int(fs)
    elif len(str(num1)) < len(str(num2)):
        zta = len(str(num2)) - len(str(num1))
        nnum1 = zta*'0' + str(num1)
        ln1 = [int(i) for i in (nnum1)]
        ln2 = [int(i) for i in str(num2)]
        for i in range(len(ln1)):
            sum = ln1[i]+ln2[i]
            sl.append(sum)
        for i in sl:
            fs += str(i)
        return int(fs)
    elif len(str(num1)) > len(str(num2)):
        zta = len(str(num1)) - len(str(num2))
        nnum2 = zta*'0' + str(num2)
        ln1 = [int(i) for i in str(num1)]
        ln2 = [int(i) for i in (nnum2)]
        for i in range(len(ln1)):
            sum = ln1[i]+ln2[i]
            sl.append(sum)
        for i in sl:
            fs += str(i)
        return int(fs)
