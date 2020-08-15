def solve(s):
    out1 = ''.join(i if i in 'aeiou' else ' ' for i in s)
    out2 = out1.split()
    il = [len(i) for i in out2]
    return max(il)