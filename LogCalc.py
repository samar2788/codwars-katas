a = [True, True, False]
op='AND'
l=[]
stra=''
opl = len(op)
opl=opl+2
for i in a:
    if i == True:
        l.append('True')
    else:
        l.append('False')

for i in l:
    stra = stra + i + " " +op.lower()+ " "

if 'xor' in stra:
    stra = stra.replace("xor","^")
    print(eval(stra[:-2]))
else:
    print(eval(stra[:-opl]))


# import operator

# OPS = {
#     "AND": operator.and_,
#     "OR" : operator.or_,
#     "XOR": operator.xor
# }

# def logical_calc(array, op):
#     return reduce(OPS[op], array)