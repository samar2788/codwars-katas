import math
def cooking_time(eggs):
    if eggs==0:
        return 0
    elif eggs>0 and eggs<=8:
        return 5
    elif eggs>8 and eggs%8==0:
        return (math.floor(eggs/8))*5
    else:
        a=math.floor(eggs/8)+1
        return a*5

print(cooking_time(0), 0)
print(cooking_time(5), 5)
print(cooking_time(10), 10)