def solve(s):
    k=[]
    l=[]
    for i in range(len(s)):
        if (s[i]==" "):
            l.append(i)
        else:
            k.append(s[i])
    print(l)
    print(k)
    k.reverse()
    
    for i in range(len(l)):
        k.insert(l[i]," ")
        print(k)
    return("".join(k))

d = solve("i love codewars")
print(d)