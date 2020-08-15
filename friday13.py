import datetime
from datetime import datetime
def unlucky_days(year):
    friday13 =0
    months=range(1,13)
    for y in range(year, year+1):
        for month in months:
            if datetime(y, month, 13).weekday() == 4:
                friday13 +=1
    return friday13

d = unlucky_days(2015)
print(d)