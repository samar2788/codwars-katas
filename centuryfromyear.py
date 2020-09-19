def century(year):

    # No negative value is allow for year
    if (year <= 0):
        return ("0 and negative is not allow for a year")

    # If year is between 1 to 100 it
    # will come in 1st century
    elif (year <= 100):
        return (1)
    elif (year % 100 == 0):
        return (year // 100)
    else:
        return (year // 100 + 1)
