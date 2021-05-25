def bmi(weight, height):
    bm=(weight/height**2)
    if bm<=18.5:
        return "Underweight"
    elif bm>18.5 and bm<=25.0:
        return "Normal"
    elif bm>25.0 and bm<=30.0:
        return "Overweight"
    else:
        return "Obese"