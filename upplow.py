a = "codE"
uc = 0
lc = 0
for i in a:
    if i.isupper():
        uc +=1
    elif i.islower():
        lc +=1

if uc > lc:
    a = a.upper()
    print(a)
elif lc > uc:
    a = a.lower()
    print(a)
else:
    a = a.lower()
    print(a)