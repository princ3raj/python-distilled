

def hello(decorator):
    def wrapped_f(f):
        print(f)
        g = decorator(f)
        g.__name__ = decorator.__name__
        print(g)
        return g
    return wrapped_f


@hello
def fun(a):
    print("HI fun()",a)

fun(8)