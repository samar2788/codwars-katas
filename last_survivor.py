def last_survivor(letters, coords):
    l=[]
    s=''
    l[:0]=letters
    for i in coords:
        l.pop(i)
    for i in l:
        s+=i
    return s

print(last_survivor('abc',[0,1]))