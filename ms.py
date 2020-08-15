def past(h,m,s):
    if 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
        if h == 0 and m!=0 and s!=0:
            return (m*60+s)*1000
        elif h!=0 and m==0 and s!=0:
            return (h*60*60+s)*1000
        elif h!=0 and m!=0 and s==0:
            return((h*60*60)+(m*60))*1000
        elif h==0 and m==0 and s==0:
            return 0
        else:
            return ((h*60*60)+(m*60)+s)*1000

d = past(1,0,1)
print(d)