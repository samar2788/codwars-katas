def parts_sums(ls, fl=[]):

    if len(ls) > 0:
        fl.append(sum(ls))
        ls.pop(0)
        return parts_sums(ls, fl)
    else:
        fl.append(0)
    return fl


print(parts_sums([744125, 935, 407, 454, 430,
                  90, 144, 6710213, 889, 810, 2579358]))
