def catch_sign_change(lst):
    al = len(lst)
    cnt =0
    for i in range(al-1):
        if(lst[i] >= 0 and lst[i+1]<0) or (lst[i]<0 and lst[i+1]>=0):
            cnt+=1
    return cnt