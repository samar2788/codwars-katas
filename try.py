import itertools
def str_to_hash(st):
    d={}
    o=[]
    e=[]
    if st=='':
        return {}
    else:
        st=st.split('=')
        st=','.join(st)
        st=st.split(',')
        for i in range(len(st)):
            if i%2==0:
                e.append(st[i].lstrip())
            else:
                o.append(st[i].lstrip())
    for i,j in zip(e,o):
        d[i]=int(j)
    return d


print(str_to_hash("a=1, b=2, c=3, d=4"), { 'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(str_to_hash(""), {})
