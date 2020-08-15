l = [1,1,4,5,1,2,1]
ul=list(set(l))

while (len(l) != len(ul)):
    for i in range(len(ul)):
        cnt = l.count(ul[i])
        if cnt > 1:
            idx = l.index(ul[i])
            l.pop(idx)
print(l)