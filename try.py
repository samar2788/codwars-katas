def convert(s):
    w2n = dict(zip(dict.fromkeys(s.upper()), '1023456789'))
    return int('0' + ''.join([w2n[ch] for ch in s.upper()]))

# def convert(st):
#     d={}
#     for i in range(len(st)):
#         if i==0:
#             d[st[i]]=1
#         elif i==1 and st[i] not in d.keys():
#             d[st[i]]=0
#         elif st[i] not in d.keys():
#             d[st[i]]=i
#     print(d)
#     for key in d.keys():
#         if key.upper() in d.keys():
#             d[key.upper()]=d[key]
    # l=[]
    # for i in st:
    #     if i in d.keys():
    #         l.append(d[i])
    # s = [str(i) for i in l]
    # res=int("".join(s))
    # return res

# 10231456354
print(convert("hChreuIueeI"))
# 10134565446 should equal 10123454335
print(convert("KATA"))
print(convert("KaTA"))
