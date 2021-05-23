def mean(town, strng):
    data = transform_datas(strng, town)
    return sum(data)/len(data)


def variance(town, strng):
    data = transform_datas(strng, town)
    if len(data) != 1:
        return sum([i ** 2 for i in data])/len(data) - mean(town, strng) ** 2
    return -1.0


def transform_datas(data, city='Rome'):
    data_transform = data.split(':')
    new_data, df = [], {}
    for i in data_transform:
        new_data.extend(i.split('\n'))
    
    for i in range(0,len(new_data)-1,2):
        df[new_data[i]] = [i[4:] for i in new_data[i+1].split(',')]
    
    curr_city = df.get(city, [-1])
    return list(map(float, curr_city))