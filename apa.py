def array_plus_array(arr1,arr2):
    l =[arr1, arr2]
    sum=0
    for i in l:
        for j in i:
            sum+=j
    return sum

d=array_plus_array([0, 0, 0], [4, 5, 6])
print(d)