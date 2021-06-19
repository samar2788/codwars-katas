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