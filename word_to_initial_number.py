def convert(s):
    w2n = dict(zip(dict.fromkeys(s.upper()), '1023456789'))
    return int('0' + ''.join([w2n[ch] for ch in s.upper()]))