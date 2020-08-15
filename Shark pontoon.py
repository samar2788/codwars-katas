def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    t1=0
    t2=0
    t1 = int(pontoon_distance/you_speed)
    print(t1)
    if dolphin == True:
        shark_speed = shark_speed/2
        t2 = int(shark_distance / shark_speed)
        print(t2)
    elif dolphin == False:
        t2 = int(shark_distance / shark_speed)
        print(t2)

    if t1 > t2:
        return "Shark Bait!"
    else:
        return "Alive!"

d=shark(46, 162, 1, 11, False)
print(d)