"""
>>> 2 + 2
4
>>> print('hi')
hi
>>> list(range(5))
[0, 1, 2,
3, 4]
>>> list(range(5))
[0, 1, 2, \
3, 4]
>>> list(range(5)) #doctest: +NORMALIZE_WHITESPACE
[0, 1, 2,
3, 4]
>>> 3 / 0 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
ZeroDivisionError: division by zero
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
