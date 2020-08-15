def accum(a):
    c =1
    l=[]
    s=''
    for i in a:
        b=c*i
        l.append(b.capitalize())
        l.append('-')
        c+=1
    for i in l:
        s+=''.join(i)
    return(s.strip('-'))