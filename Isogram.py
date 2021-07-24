def is_isogram(string):
    if string == "":
        return True
    else:
        string = string.lower()
        d = {}
        for i in range(len(string)):
            if string[i] in d.keys():
                d[string[i]] += 1
            else:
                d[string[i]] = 1
        for k, v in d.items():
            if v > 1:
                return False
        return True
