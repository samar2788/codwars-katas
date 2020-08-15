def next_id(arr):
    for i in range(len(arr)+1):
        if i not in arr:
            return i


d = next_id([])
print(d)