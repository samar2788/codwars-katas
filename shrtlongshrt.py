def solution(a, b):
    la = len(a)
    lb = len(b)
    
    if la > lb:
        return b+a+b
    else:
        return a+b+a