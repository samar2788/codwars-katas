import re
def change(s, prog, version):
    # print(s)
    # print(prog)
    # print(version)
    s = s.split('\n')
    l = []
    for i in s:
        if 'title' in i:
            l.append(f"Program: {prog}")
        elif 'Author' in i:
            l.append("Author: g964")
        elif 'Phone' in i:
            i = i.split(' ')
            i = i[1].split('-')
            if '+1' in i[0] and len(i[1]) == 3 and len(i[2]) == 3 and len(i[3]) == 4:
                l.append("Phone: +1-503-555-0090")
            else:
                return ("ERROR: VERSION or PHONE")
        elif 'Date' in i:
            l.append("Date: 2019-01-01")
        elif 'Version' in i:
            print(i)
            if 'Version: 2.0' in i:
                l.append("Version: 2.0")
            elif re.match('\/Version:\s\d+\.\d+', i)==False:
                return "ERROR: VERSION or PHONE"
            else:
                l.append(f"Version: {version}")
    st = ' '.join(l)
    return st


s1 = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-0091\nDate: Tues April 9, 2005\nVersion: 67\nLevel: Alpha'
s11 = 'Program title: Hammer\nAuthor: Tolkien\nCorporation: IB\nPhone: +1-503-555-0090\nDate: Tues March 29, 2017\nVersion: 2.0\nLevel: Release'
s12 = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-009\nDate: Tues April 9, 2005\nVersion: 6.7\nLevel: Alpha'

# print
print(change(s1, 'Ladder', '1.1'),'Program: Ladder Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 1.1')
#print(change(s11, 'Balance', '1.5.6'), 'Program: Balance Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 2.0')
#print(change(s12, 'Ladder', '1.1'), 'ERROR: VERSION or PHONE')
