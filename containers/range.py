def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''
    import math
    if b is None and c is None:
        i = 1
        tby = -1
        while i <= a:
            i += 1
            tby += 1
            yield tby
    if b and c is None:
        i = 1
        tby = a - 1
        while i <= b - a:
            i += 1
            tby += 1
            yield tby
    if b and c:
        i = 1
        tby = a - c
        while i <= math.ceil((b - a) / c):
            i += 1
            tby += c
            yield tby
