def likes(names):
    if len(names) == 0:
        return "no one likes this"
    if len(names) == 1:
        return names[0]+" likes this"
    if len(names) == 2:
        return names[0] + ' and ' + names[1] + " like this"
    if len(names) == 3:
        return names[0] + ', '+names[1]+' and '+names[2] + ' like this'
    if len(names) > 3:
        d = len(names)-2
        return names[0] + ', '+names[1]+' and '+str(d) + ' others like this'
