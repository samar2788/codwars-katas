import math
a ="xxxxxYxYx"
l=a.split('Y')
w=2
cnt=0

for i in l:
    d= math.ceil((len(i)/w))
    cnt +=d

print(cnt)