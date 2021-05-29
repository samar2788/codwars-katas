def travel(r, zipcode):
    if zipcode == '':
        return ":/"
    if zipcode not in r:
        return f"{zipcode}:/"
    if zipcode in r and len(zipcode) != 8:
        return f"{zipcode}:/"
    else:
        r = r.split(',')
        l = []
        hnum = []
        ad = []
        c = 0
        for i in r:
            if zipcode in i:
                l.append(i)
        for i in l:
            li = len(i)
            for j in i:
                if j == ' ':
                    break
                else:
                    c += 1
            hnum.append(i[0:c])
            ad.append(i[(c+1):-9])
            c = 0
        ad = ','.join(ad)
        hnum = ','.join(hnum)
        return f"{zipcode}:{ad}/{hnum}"
