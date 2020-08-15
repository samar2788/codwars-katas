def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            print(i)
            sum += i
        elif '':
            sum = 0
    return sum

d = positive_sum([-1,-2,-3,-4,-5])
print(d)