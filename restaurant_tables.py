def restaurant(single_tables, double_tables, visitors):
    kicked = 0
    half = 0
    for i in visitors:
        if i == 1:
            if single_tables > 0:
                single_tables -= 1
            elif double_tables > 0:
                double_tables -= 1
                half += 1
            elif half > 0:
                half -= 1
            else:
                kicked += 1 
        if i == 2:
            if double_tables > 0:
                double_tables -= 1
            else:
                kicked += 2
    return kicked