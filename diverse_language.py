def is_language_diverse(lst):
    d={}
    for i in lst:
        if i['language'] not in d.keys():
            d[i['language']]=1
        else:
            d[i['language']] += 1
    value=d.values()
    l=list(value)
    l.sort(reverse=True)
    for i in range(1,len(l)):
        if l[0] > l[i]*2:
            return False
    return True

list1 = [
    {'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba',
     'continent': 'Americas', 'age': 42, 'language': 'Python'},
    {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus',
     'continent': 'Europe', 'age': 22, 'language': 'Ruby'},
    {'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan',
     'continent': 'Asia', 'age': 43, 'language': 'Ruby'},
    {'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary',
     'continent': 'Europe', 'age': 95, 'language': 'JavaScript'},
    {'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica',
     'continent': 'Americas', 'age': 18, 'language': 'JavaScript'},
    {'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal',
     'continent': 'Europe', 'age': 25, 'language': 'JavaScript'}
]

list2 = [
    {'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba',
        'continent': 'Americas', 'age': 42, 'language': 'Python'},
    {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus',
     'continent': 'Europe', 'age': 22, 'language': 'Ruby'},
    {'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary',
     'continent': 'Europe', 'age': 95, 'language': 'JavaScript'},
    {'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica',
     'continent': 'Americas', 'age': 18, 'language': 'JavaScript'},
    {'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal',
     'continent': 'Europe', 'age': 25, 'language': 'JavaScript'}
]

list3 = [
    {'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba',
        'continent': 'Americas', 'age': 42, 'language': 'Python'},
    {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus',
     'continent': 'Europe', 'age': 22, 'language': 'Ruby'},
    {'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica',
     'continent': 'Americas', 'age': 18, 'language': 'JavaScript'},
    {'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal',
     'continent': 'Europe', 'age': 25, 'language': 'JavaScript'}
]

list4 = [
    {'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba',
        'continent': 'Americas', 'age': 42, 'language': 'Python'},
    {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus',
     'continent': 'Europe', 'age': 22, 'language': 'Ruby'},
    {'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal',
     'continent': 'Europe', 'age': 25, 'language': 'JavaScript'}
]

is_language_diverse(list1)
is_language_diverse(list2)
is_language_diverse(list3)
is_language_diverse(list4)
