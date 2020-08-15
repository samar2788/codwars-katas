import json


def get_strings(city):
    city = city.lower()
    s = {}
    for i in city:
        if i == " ":
            pass
        elif i in s:
            s[i] += '*'
        else:
            s[i] = '*'
    strs = json.dumps(s)
    strs = strs.replace('{', '').replace('}', '').replace(
        '"', '').replace(' ', '')
    return strs