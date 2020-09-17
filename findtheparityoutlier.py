def find_outlier(a):
    co = 0
    ce = 0
    for i in a:
        if i % 2 == 0:
            ce += 1
        else:
            co += 1

    if ce == 1:
        for i in a:
            if i % 2 == 0:
                return i
    elif co == 1:
        for i in a:
            if i % 2 != 0:
                return i
