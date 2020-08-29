def find_the_number_plate(customer_id):
    q, r = divmod(customer_id, 999)
    q, a = divmod(q, 26)
    c, b = divmod(q, 26)
    return f"{chr(a+97)}{chr(b+97)}{chr(c+97)}{r+1:03d}"
