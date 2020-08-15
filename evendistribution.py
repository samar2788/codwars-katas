def distribute_evenly(lst):
    d = {i:lst.count(i) for i in lst}
    print(d)
    
    cnt = 0
    res = []
    print(max(d.values()))
    while max(d.values())>cnt:
        res += [k for k,v in d.items() if v>cnt]
        print(res)
        cnt += 1
    
    return res