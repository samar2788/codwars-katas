def pluck(objs, name):
    lo = len(objs)
    fl = []
    for i in range(lo):
        if name in objs[i]:
            fl.append(objs[i][name])
        elif name not in objs[i]:
            fl.append(None)
    return fl
