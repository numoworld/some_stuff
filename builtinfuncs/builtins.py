def map(func, arr):
    """Applies function func() to each element of iterable arr"""
    if func is None:
        raise Exception
    if arr is None:
        raise Exception
    it = iter(arr)
    while True:
        try:
            yield func(next(it))
        except StopIteration:
            return


def zip(*args):
    """Converts multiple iterables to iterator of tuples of
    corresponding elements from iterables"""
    if args is None or len(args) == 1:
        raise Exception

    iters = [iter(it) for it in args]
    while True:
        try:
            yield tuple([next(it) for it in iters])
        except StopIteration:
            return


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
