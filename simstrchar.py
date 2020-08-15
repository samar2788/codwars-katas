def solve(s):
    cntU =0
    cntL =0
    cntN =0
    cntO =0
    flist = []
    for i in s:
        if i.isupper():
            cntU+=1
        elif i.islower():
            cntL+=1
        elif i.isnumeric():
            cntN+=1
        elif i is None:
            pass
        else:
            cntO+=1
    
    flist.extend([cntU,cntL,cntN,cntO])
    return flist

d = solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD")
print(d)