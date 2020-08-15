def first_non_consecutive(arr):
    seed = arr.pop(0)
    for num in arr:
        seed +=1
        if num != seed:
            return num
    return None


d = first_non_consecutive([31,32,34])
print(d)
