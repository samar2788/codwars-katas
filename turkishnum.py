def get_turkish_number(num):
    td = {
        0: "sıfır",
        1: "bir",
        2: "iki",
        3: "üç",
        4: "dört",
        5: "beş",
        6: "altı",
        7: "yedi",
        8: "sekiz",
        9: "dokuz",
        10: "on",
        20: "yirmi",
        30: "otuz",
        40: "kırk",
        50: "elli",
        60: "altmış",
        70: "yetmiş",
        80: "seksen",
        90: "doksan"
    }

    if num <= 10:
        return td[num]
    elif num > 10 and num % 10 != 0:
        tens = num/10
        a, b, c = str(tens)
        t = int(a)*10
        o = int(c)
        return td[t] + ' ' + td[o]
    else:
        return td[num]


print(get_turkish_number(90))
