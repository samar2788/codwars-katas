def dative(word):
    for c in word[::-1]:
        if c in u'eéiíöőüű':
            return word+'nek'
        elif c in u'aáoóuú':
            return word+'nak'


# a = "virág"

# fv = 'e, é, i, í, ö, ő, ü, ű'
# bv = 'a, á, o, ó, u, ú'
# fl = []
# bl = []

# for i in a:
#     if i in bv:
#         bl.append(a.rindex(i))
# for i in a:
#     if i in fv:
#         fl.append(a.rindex(i))

# if len(bl) == 0 and len(fl) > 0:
#     print(a+"nek")
# elif len(fl) == 0 and len(bl) > 0:
#     print(a+"nak")
# elif len(bl) > 0 and len(fl) > 0:
#     bl.sort(reverse=True)
#     fl.sort(reverse=True)
#     if bl[0] > fl[0]:
#         print(a+"nak")
#     elif fl[0] > bl[0]:
#         print(a+"nek")
