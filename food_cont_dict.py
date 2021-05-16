def order_food(lst):
    s={}
    for i in lst:
        if i['meal'] not in s:
            s[i['meal']]=1
        else:
            s[i['meal']]+=1
    return s