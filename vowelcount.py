def get_count(input_str):
    c = 0
    for i in input_str:
        if i in 'aeiou':
            c += 1
    return c
