def mxdiflg(a1, a2):
    if a1 !=[] and a2 !=[]:
        mins1 = min(len(i) for i in a1)
        maxs2 = max(len(i) for i in a2)
        diff1 = abs(maxs2 - mins1)
        maxs1 = max(len(i) for i in a1)
        mins2 = min(len(i) for i in a2)
        diff2 = abs(maxs1 - mins2)
        if diff1 > diff2:
            return diff1
        else:
            return diff2
    else:
        return -1