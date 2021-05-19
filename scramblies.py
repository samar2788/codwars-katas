def scramble(s1, s2):
    d={}
    l={}
    c=0
    for i in range(len(s1)):
        if s1[i] not in d.keys():
            d[s1[i]]=1
        else :
            d[s1[i]] +=1
    print(d)
    for i in range(len(s2)):
        if s2[i] not in l.keys():
            l[s2[i]]=1
        else:
            l[s2[i]]+=1
    print(l)
    for key in l.keys():
        if key in d.keys() and l[key]<=d[key]:
            continue
        else:
            return False
    return True



print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))
print(scramble('scriptjavx', 'javascript'))
