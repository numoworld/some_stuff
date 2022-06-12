def find_index(elements, value):
    """Searches for an element with given value and returns its index
    or -1 if there's no such index"""

    if elements is None:
        raise Exception

    for idx, elem in enumerate(elements):
        if elem == value:
            return idx

    return -1


# NOTE: Native 'in' operator is more than 10x faster than search.linear.contains()
# >>> import timeit
# >>> from search.linear import contains
# >>> fruits = ['orange', 'plum', 'banana', 'apple']
# >>> timeit.timeit(lambda: contains(fruits, 'blueberry'))
# 1.8904765040024358
# >>> timeit.timeit(lambda: 'blueberry' in fruits)
# 0.22473459799948614
# NOTE: The 'in' operator doesn't always do a linear search. When you use it
# on a set, for example, it does a hash-based search instead.
def contains(elements, value):
    """Returns True if iterable elements contains element with given value"""

    if elements is None:
        raise Exception

    for elem in elements:
        if elem == value:
            return True

    return False

