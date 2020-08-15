def solve(arr):
    
    p, q = 1, 1
    
    for k in arr:
        
        x, y = max(k), min(k)
        
        a = p * x
        b = q * x
        c = p * y
        d = q * y
        
        p = max(a, b, c, d)
        q = min(a, b, c, d)
            
    return max(p, q)

d = solve([[-11,-6],[-20,-20],[18,-4],[-20, 1]])
print(d)