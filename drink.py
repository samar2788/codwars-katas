def get_drink_by_profession(param):
    word = param.lower()
    if word == "jabroni":
        return "Patron Tequila"
    elif word == "school counselor":
        return "Anything with Alcohol"
    elif word == "programmer":
        return "Hipster Craft Beer"
    elif word == "bike gang member":
        return "Monshine"
    elif word == "politician":
        return "Your tax dollars"
    elif word == "rapper":
        return "cristal"
    else:
        return "Beer"

d = get_drink_by_profession("JabRoni")
print(d)