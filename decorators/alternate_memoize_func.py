# note that this decorator ignores **kwargs
from textwrap import wrap


def memoize_v1(obj):
    cache = obj.cache = {}

    @wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer

# Here's a modified version that also respects kwargs.
def memoize_v2(obj):
    cache = obj.cache = {}

    @wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer

def wraps(decorator):

    wraps.__name__ = decorator.__name__
    wraps.__doc__ = decorator.__doc__
    return wraps


@memoize_v1
def sum(a,b):
    return a + b

@memoize_v2
def multiply(a,b):
    '''Multiplication of two numbers'''
    return a * b

print(sum(2345,789))
print(multiply(23456,98764))

print(multiply.__doc__)

