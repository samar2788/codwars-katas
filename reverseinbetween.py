def reverse(st, a, b) : 
    print(len(st))
    # Invalid range  
    if (b >= len(st)) : 
        b=len(st)-1
        print(b)
    st = list(st) 
    # While there are characters to swap  
    while (a <= b) : 

        # Swap(str[l], str[r])  
        c = st[a]  
        st[a] = st[b]  
        st[b] = c  

        a += 1;  
        b -= 1;  
    return "".join(st)  

print(reverse('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',6,56))

# def solve(s,a,b):
#     return s[:a]+s[a:b+1][::-1]+s[b+1:]