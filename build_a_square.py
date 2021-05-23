def generate_shape(n):
    s=''
    for i in range(n):
        s+=(n*'+')
        if i !=(n-1):
            s+='\n'
    return s

print(generate_shape(8))