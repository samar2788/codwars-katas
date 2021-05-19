def row_weights(array):
    e=[]
    o=[]
    for i in range(len(array)):
        if i%2==0:
            e.append(array[i])
        else:
            o.append(array[i])
    es=sum(e)
    os=sum(o)
    return (es,os)