def disemvowel(a):
    for i in a:
        if i in 'aeiouAEIOU':
            a = a.replace(i, '')
    return a
#Alternative solution


# def disemvowel(s):
#     return s.translate(None, "aeiouAEIOU")
