def find_admin(lst, lang):
    s = []
    for i in lst:
        if i['language'] == lang and i['githubAdmin'] == 'yes':
            s.append(i)
    return s
