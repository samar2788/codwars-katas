def even_last(numbers):
    l=[]
    if len(numbers)==0:
        return 0
    else:
        for i in range(len(numbers)):
            if i%2==0:
                l.append(numbers[i])
    ls=sum(l)
    return ls*numbers[-1]