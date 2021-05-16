import re
l = []


def camelize(s):
    f = ''
    n = separate(s)
    d = []
    global l
    l = []
    for i in n:
        if i[0].isdigit() or i[0].isalpha() == False:
            d.append(i.title())
        else:
            d.append(i.capitalize())
    f = ''.join(d)
    res = re.sub('[\W_]+', '', f)
    return res


def separate(s):
    pos = 1
    while pos < len(s) and (s[pos].isalpha() or s[pos].isdigit()):
        pos += 1
    l.append(s[:pos])
    if s[(pos+1):]:
        separate(s[(pos+1):])
    return l


print(camelize("'quOted'= > 'What'"))
print(camelize("your-name-here"))



''' Below is an alternative solution to the problem i dont know if that works as i am not able to find the kata now'''

l = []


def test(s):
    pos = 1
    while pos < len(s) and (s[pos].isalpha() or s[pos].isnumeric()):
        pos += 1
    temp = s[:pos]
    res = re.sub('[\W_]+', '', temp)
    l.append(res)
    s = s[(pos+1):]
    if s:
        test(s)
    return l


def camelize(s):
    n = test(s)
    global l
    l = []
    b = []
    a = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in n]
    for i in a:
        b.append(i.title())
    return (''.join(b))
