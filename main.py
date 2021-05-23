import collections
from typing import Iterable

import pytest


def ilen(iterable: Iterable):
    size = 0
    for _ in iterable:
        size += 1
    return size


def test_ilen_1():
    assert ilen(x for x in range(10)) == 10


def test_ilen_2():
    assert ilen([1, [7, 48], 7]) == 3


def test_ilen_3():
    assert ilen("string") == 6


def test_ilen_4():
    with pytest.raises(TypeError):
        assert ilen(5)


def test_ilen_5():
    with pytest.raises(TypeError):
        assert ilen()


def flatten(iterable: Iterable):
    for x in iterable:
        if hasattr(x, '__iter__') and type(x) is not str:
            for y in flatten(x):
                yield y
        else:
            yield x


def test_flatten_1():
    assert list(flatten(x for x in range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_flatten_2():
    assert list(flatten([0, [1, [2, [4, 3]]]])) == [0, 1, 2, 4, 3]


def test_flatten_3():
    assert list(flatten("string")) == ['s', 't', 'r', 'i', 'n', 'g']


def test_flatten_4():
    with pytest.raises(TypeError):
        assert list(flatten(5))


def test_flatten_5():
    with pytest.raises(TypeError):
        assert list(flatten())


def distinct(iterable: Iterable):
    c = collections.Counter()
    for word in iterable:
        c[word] += 1
    for unic in c:
        yield unic


def test_distinct_1():
    assert list(distinct(x for x in range(10))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_distinct_2():
    assert list(distinct([1, 2, 0, 1, 3, 0, 2])) == [1, 2, 0, 3]


def test_distinct_3():
    assert list(distinct("test string")) == ['t', 'e', 's', ' ', 'r', 'i', 'n', 'g']


def test_distinct_4():
    with pytest.raises(TypeError):
        assert list(distinct(5))


def test_distinct_5():
    with pytest.raises(TypeError):
        assert list(distinct())


def groupby(key, iterable: Iterable):
    group = {}
    for dictionary in iterable:
        assert key in dictionary.keys(), "Такого ключа нет в словаре"
        if dictionary[key] not in group.keys():
            some_list = [dictionary]
            group[dictionary[key]] = some_list
        else:
            group[dictionary[key]].append(dictionary)
    return group


users = [
    {'gender': 'female', 'age': 33},
    {'gender': 'male', 'age': 20},
    {'gender': 'female', 'age': 21},
]


def test_groupby_1():
    assert groupby("gender", users) == {'female': [{'gender': 'female', 'age': 33},
                                                   {'gender': 'female', 'age': 21}],
                                        'male': [{'gender': 'male', 'age': 20}]}


def test_groupby_2():
    assert groupby("age", users) == {33: [{'gender': 'female', 'age': 33}],
                                     20: [{'gender': 'male', 'age': 20}],
                                     21: [{'gender': 'female', 'age': 21}]}


def test_groupby_3():
    with pytest.raises(AssertionError):
        assert groupby("name", users)


def test_groupby_4():
    with pytest.raises(AttributeError):
        assert groupby("age", ["users", "age", "gender"])


def test_groupby_5():
    with pytest.raises(TypeError):
        assert groupby()


def chunks(size: int, iterable: Iterable):
    assert size > 0, "размер должен быть больше нуля"
    some_list = []
    i = 0
    for x in iterable:
        some_list.append(x)
        i += 1
        if i == size:
            yield tuple(some_list)
            i = 0
            some_list.clear()
    if some_list:
        yield tuple(some_list)


def test_chunks_1():
    assert list(chunks(3, [0, 1, 2, 3, 4, 7, 3, 56])) == [(0, 1, 2), (3, 4, 7), (3, 56)]


def test_chunks_2():
    assert list(chunks(20, [0, 1, 2, 3, 4, 7, 3, 56])) == [(0, 1, 2, 3, 4, 7, 3, 56)]


def test_chunks_3():
    with pytest.raises(AssertionError):
        assert list(chunks(-20, [0, 1, 2, 3, 4, 7, 3, 56]))


def test_chunks_4():
    assert list(chunks(2, "string")) == [('s', 't'), ('r', 'i'), ('n', 'g')]


def test_chunks_5():
    with pytest.raises(TypeError):
        assert list(chunks(2, 2))


def first(iterable: Iterable):
    return next(iter(iterable), None)


def test_first_1():
    assert first(x for x in range(10)) == 0


def test_first_2():
    assert first("string") == 's'


def test_first_3():
    assert first(range(0)) is None


def test_first_4():
    with pytest.raises(TypeError):
        assert first(5)


def test_first_5():
    assert first("") is None


def last(iterable: Iterable):
    if not iterable:
        return None
    *_, last_el = iterable
    return last_el


def test_last_1():
    assert last(x for x in range(10)) == 9


def test_last_2():
    assert last("string") == 'g'


def test_last_3():
    assert last(range(0)) is None


def test_last_4():
    with pytest.raises(TypeError):
        assert last(5)


def test_last_5():
    assert last("") is None


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
    print(groupby('age', users))

    print(list(chunks(3, [0, 1, 2, 3, 4, 7, 3, 56, ])))

    foo = (x for x in range(10))
    print(first(foo))
    print(first(range(0)))
    print(first(spisok))

    foo = (x for x in range(10))
    print(last(foo))
    print(last(spisok))
    print(last(range(0)))

    print(list(flatten("str")))
    print(list(flatten((3, 5, (4, 6), 3))))
