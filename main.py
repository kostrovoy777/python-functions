import collections
from typing import Iterable


def ilen(iter: Iterable):
    size = 0
    for _ in iter:
        size += 1
    return size


def flatten(iter: Iterable):
    for x in iter:
        if hasattr(x, '__iter__'):
            for y in flatten(x):
                yield y
        else:
            yield x


def distinct(iter: Iterable):
    c = collections.Counter()
    for word in iter:
        c[word] += 1
    for unic in c:
        yield unic


def groupby(key, iter: Iterable):
    group = {}
    for dict in iter:
        if dict[key] not in group.keys():
            some_list = [dict]
            group[dict[key]] = some_list
        else:
            group[dict[key]].append(dict)
    return group


def chunks(size: int, iter: Iterable):
    some_list = []
    i = 0
    for x in iter:
        some_list.append(x)
        i += 1
        if i == size:
            yield tuple(some_list)
            i = 0
            some_list.clear()
    if some_list:
        yield tuple(some_list)


if __name__ == '__main__':
    foo = (x for x in range(10))
    print(ilen(foo))
    spisok = [1, [7, 48], 7]
    print(ilen(spisok))

    print(list(flatten([0, [1, [2, [4, 3]]]])))
    foo = (x for x in range(10))
    print(list(flatten(foo)))
    print(list(distinct([1, 2, 0, 1, 3, 0, 2])))

    users = [
        {'gender': 'female', 'age': 33},
        {'gender': 'male', 'age': 20},
        {'gender': 'female', 'age': 21},
    ]
    print(groupby('gender', users))

    print(list(chunks(6, [0, 1, 2, 3, 4, 7, 3, 56, 8, 9, 6, 4,5,6])))
