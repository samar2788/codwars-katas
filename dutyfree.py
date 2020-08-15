def duty_free(price, discount, holiday_cost):
    afterdiscount = (price * discount) / 100
    dutyfreeBottles = int(holiday_cost/afterdiscount)
    return dutyfreeBottles

d = duty_free(17, 10, 500)
print(d)