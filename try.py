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


#  if bmi <= 18.5 return "Underweight"


# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"
