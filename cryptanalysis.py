a = "Hippopotomonstrosesquippedaliophobia"
a = a.lower()
print(a)
cod = {}
cd = 0
for i in a:
    if i not in cod:
        cod[i] = cd
        cd += 1
a = '.'.join(a)
print(a)
for i in a:
    if i in cod.keys():
        a = a.replace(i, str(cod[i]))
print(a)
