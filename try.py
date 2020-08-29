a = ['a', 'a', 'b', 'b', 'c', 'a', 'b', 'c', 'c']
indices = [i for i, x in enumerate(a) if x == 'b']
print(indices)
for i ,x in enumerate(a):
    print(i,x)