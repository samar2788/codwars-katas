def solve(arr):
    print(arr)
    j=[sorted(i, key=abs) for i in arr]
    jl = len(j)
    l=[]
    result=1
    for i in range(jl):
        tmpjl = len(j[i])
        l.append(j[i][tmpjl-1])
    for i in l:
        result*=i
    return(result)
    

solve([[10,-15],[-1,-3]])