def balance_statement(lst):
    buy = []
    sell = []
    sumbuy = 0
    sumsell = 0
    errl = []
    err = 0
    if lst == '':
        return "Buy: 0 Sell: 0"
    elif lst != '':
        ls = lst.split(', ')
        for i in ls:
            tl = i.split(' ')
            tll = len(tl)
            if tll != 4 or '.' in tl[1] or '.' not in tl[2] or tl[0] == '' or tl[3] == '' or tl[3] not in 'BS':
                err += 1
                errl.append(i)
            else:
                if tl[3] == 'B':
                    tt = float(tl[1])*float(tl[2])
                    buy.append(tt)
                elif tl[3] == 'S':
                    tt = float(tl[1])*float(tl[2])
                    sell.append(tt)
    sumbuy = round(sum(buy))
    sumsell = round(sum(sell))
    ers = ' ;'.join(errl)
    if err > 0:
        return f"Buy: {sumbuy} Sell: {sumsell}; Badly formed {err}: {ers} ;"
    else:
        return f"Buy: {sumbuy} Sell: {sumsell}"


print(balance_statement(
    "ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B"))

print(balance_statement(
    "GOOG 90 160.45 B, JPMC 67 12.8 S, MYSPACE 24.0 210 B, CITI 50 450 B, CSCO 100 55.5 S"))
# "Buy: 29499 Sell: 0")
