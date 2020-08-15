def count_ways(n, k):  
      
    temp = 0
    res = [1]  
      
    for i in range(1, n + 1): 
        s = i - k - 1
        e = i - 1
        if (s >= 0): 
            temp -= res[s]  
        temp += res[e]  
        res.append(temp)  
          
    return res[n] 

d =count_ways(14,7)
print(d)