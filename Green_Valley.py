def make_valley(arr):
    left=[]
    right=[]
    sa=sorted(arr,reverse=True)
    for i in range(len(sa)):
        if i%2==0:
            left.append(sa[i])
        else:
            right.append(sa[i])
    fl=left + sorted(right)
    return fl