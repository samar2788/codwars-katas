def over_the_road(address, n):
    lists = list(range(1,((2*n)+1)))
    odd = list(filter(lambda x: x%2==1,lists))
    even = list(filter(lambda x: x%2==0,lists))
    even.reverse()
    ml = tuple(zip(odd,even))

    for x,y in ml:
        if x==address:
            return y
        elif y==address:
            return x

a = over_the_road(4778098276,21582033789)
print(a)

# def over_the_road(address, n):
#     '''
#     Input: address (int, your house number), n (int, length of road in houses) 
#     Returns: int, number of the house across from your house. 
#     '''
#     # this is as much a math problem as a coding one 
#     # if your house is [even/odd], the opposite house will be [odd/even] 
#     # highest number on street is 2n 
#     # Left side houses are [1, 3, ... 2n-3, 2n-1] 
#     # Right side houses are [2n, 2n-2, ... 4, 2] 
#     # Sum of opposite house numbers will always be 2n+1 
#     return (2*n + 1 - address) 