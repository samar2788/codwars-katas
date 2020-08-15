a = [3, 0, 1, 3, 2, 1, 0, 0, 3, 4, 2, 0, 3, 0, 2, 0, 0, 1, 2, 2, 0, 2, 2, 0, 4, 3, 4]
line=0
level=1
pt=0
for i in a:
    line+=i
    
    if line>10:
        level+=1
        line=0

    if i == 0:
        pt+=0
        print(pt)
    elif i == 1:
        pt+=(40*level)
        print(pt)
    elif i==2:
        pt+=(100*level)
        print(pt)
    elif i==3:
        pt+=(300*level)
        print(pt)
    elif i==4:
        pt+=(1200*level)
        print(pt)

print(pt)