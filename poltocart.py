import math
def coordinates(degrees, radius):
    degrees = degrees * math.pi/180.0

    x = radius * math.cos(degrees)
    y = radius * math.sin(degrees)

    return (round(x,10), round(y,10))

d = coordinates(45, 1)
print(d)