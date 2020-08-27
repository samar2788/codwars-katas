def arr(n=0):
    l=[]
    if n == 0 or n==None or n=='':
        return []
    else:
        for i in range(n+1):
            l.append(i)
    return l

print(arr())