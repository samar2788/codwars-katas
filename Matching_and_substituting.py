import re
def change(s, prog, version):
    print(s)
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
            if 'Version: 2.0' in i:
                l.append("Version: 2.0")
            elif re.match('Version:\s\d+\.\d+$', i)==None:
                return "ERROR: VERSION or PHONE"
            else:
                l.append(f"Version: {version}")
    st = ' '.join(l)
    return st