def game(words):
    c=0
    lw=len(words)
    if lw==0:
        return []
    elif lw==1:
        return words
    elif '' in words:
        c=words.index('')
        return words[0:c]
    elif '' not in words and lw>1:
        for i in range(lw-1):
            if words[i][-1]==words[i+1][0]:
                c+=1
            elif words[i][-1]!=words[i+1][0]:
                return words[0:(c+1)]
        diff=lw-c
        if diff==1:
            c+=1
    return words[0:c]


print(game(["dog", "goose","elephant", "tiger", "rhino", "orc", "cat"]))
print(game(["lion","notter",'']))
