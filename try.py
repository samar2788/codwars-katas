import datetime
from calendar import monthrange
a=2016
b=2020
fl=[]
m=[]

monthnames={1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}

for i in range(a,(b+1)):
    for j in range(1,13):
        d=datetime.datetime(i,j,1)
        if d.strftime(("%A"))=="Friday" and monthrange(i,j)[1]==31:
            m.append(j)
for key, val in monthnames.items():
    if m[0]==key:
        fl.append(val)

for key, val in monthnames.items():
    if m[-1] == key:
        fl.append(val)

d=(fl[0],fl[1],len(m))
print(d)