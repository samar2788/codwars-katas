def duplicate_encode(word):
    word = word.lower()
    d = {}
    l = []
    for i in range(len(word)):
        if word[i] in d.keys():
            d[word[i]] += 1
        else:
            d[word[i]] = 1
    for k, v in d.items():
        if v > 1:
            d[k] = ')'
        else:
            d[k] = '('
    for i in word:
        if i in d.keys():
            l.append(d[i])
    fs = ''.join(l)
    return fs


#print(duplicate_encode("din"), "(((")
print(duplicate_encode("recede"), "()()()")
# print(duplicate_encode("Success"),")())())","should ignore case")
# print(duplicate_encode("(( @"),"))((")
