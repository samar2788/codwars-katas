from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    pass


def ordered_count(seq):
    return list(OrderedCounter(seq).items())

a = ordered_count("abracadabra")
print(a)