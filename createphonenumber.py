def create_phone_number(n):
    s = ''
    for i in n:
        s += str(i)
    st = s[0:3]
    mid = s[3:6]
    end = s[6:]
    return '('+st+')' + ' '+mid+'-'+end

#Alternative Solution


# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
