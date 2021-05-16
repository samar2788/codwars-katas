def is_same_language(lst):
    s = {}
    s = set()
    for i in lst:
        s.add(i['language'])
    if len(s) == 1:
        return True
    else:
        return False
