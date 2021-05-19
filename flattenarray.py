def flatten_and_sort(array):
    fl=[]
    for i in array:
        for j in i:
            fl.append(j)
    return(sorted(fl))