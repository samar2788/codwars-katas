def solve(arr):
    for i in arr:
        if -i in arr and i in arr:
            pass
        else:
            return i
            break

d = solve([ -9,-105,-9,-9,-9,-9,105])
print(d)