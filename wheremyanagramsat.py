def anagrams(word, words):
    d={}
    td={}
    rl=[]
    for i in range(len(word)):
        if word[i] in d.keys():
            d[word[i]]+=1
        else:
            d[word[i]]=1
    for i in words:
        if len(i)!=len(word):
            continue
        else:
            for j in range(len(i)):
                if i[j] in td.keys():
                    td[i[j]]+=1
                else:
                    td[i[j]]=1
        if d==td:
            rl.append(i)
        td={}
    if rl==[]:
        return []
    else:
        return rl


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
