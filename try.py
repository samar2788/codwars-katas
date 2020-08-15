import json
a = "Chicago"
a=a.lower()
print(a)
s={}
for i in a :
    if i in s:
        s[i]+='*'
    else:
        s[i]='*'
strs = json.dumps(s)
strs = strs.replace('{', '').replace('}', '').replace('"', '').replace(' ', '')
print(strs)
