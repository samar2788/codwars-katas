from functools import lru_cache

@lru_cache()
def skiponacci(n):
    l=[]
    c=0
    s=''
    x, y=0,1
    while c!=n:
        l.append(y)
        x,y=y,x+y
        c+=1
    ll=len(l)
    print(ll)
    for i in range(ll):
        if i%2!=0:
            l[i]=' skip '
    for i in l:
        s+=str(i)
    
    return s.strip()
skiponacci(6)