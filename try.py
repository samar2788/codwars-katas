def meeting(rooms, number):
    temp=number
    l=[]
    if number ==0:
        return "Game On"
    for i in range(len(rooms)):
        print(l)
        if len(rooms[i][0])>rooms[i][1]:
            l.append(0)
        else:
            diff=rooms[i][1]-len(rooms[i][0])
            if diff > number:
                l.append(number)
            else:
                l.append(diff)
                number = number - diff
            if sum(l)==temp:
                return l
    return ("Not enough!")


print(meeting([['', 2], ['XXXXXXXXXX', 3], ['XXXXXXXX', 10],['', 10], ['XXX', 0], ['XX', 8], ['XXXXXXX', 5]], 8))
# print(meeting([["XXX", 3], ["XXXXX", 6], ["XXXXXX", 9]], 4), [0, 1, 3])
# print(meeting([["XXX", 1], ["XXXXXX", 6], ["X", 2], ["XXXXXX", 8], ["X", 3], ["XXX", 1]], 5), [0, 0, 1, 2, 2])
# print(meeting([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 0), "Game On")
# print(meeting([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 8), "Not enough!")
# print(meeting([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 2), [0, 2])

# print(meeting([['XXXXXX', 2], ['XXXXXXXXX', 5], ['X', 10], ['XXX', 3], ['XXXXXXXXX', 7], ['XX', 4], ['XXXXXX', 1], ['', 2], ['XXXXXXX', 0], ['XXXX', 5]], 2))

