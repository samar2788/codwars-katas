def nb_dig(n, d):
    cnt = 0
    if n >=0 and 0<=d<=9:
        for i in range(n+1):
            si = i**2
            strsi = str(si)
            strd = str(d)
            if strd in strsi:
                for j in strsi:
                    if strd == str(j):
                        cnt += 1
    return cnt


d = nb_dig(25, 1)
print(d)