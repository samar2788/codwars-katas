from collections import OrderedDict
def in_array(array1, array2):
    l=[]
    for i in array1:
        for j in array2:
            if i in j:
                l.append(i)

    fl=OrderedDict.fromkeys(l)
    return (sorted(list(fl)))

a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']

in_array(a1,a2)