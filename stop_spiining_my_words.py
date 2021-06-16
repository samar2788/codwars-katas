def spin_words(sentence):
    l=sentence.split(' ')
    d=[]
    for i in range(len(l)):
        if len(l[i])>=5:
            d.append(l[i][::-1])
        else:
            d.append(l[i])
    res=' '.join(d)
    return res