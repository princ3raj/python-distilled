def decorator_func_with_arguments(arg1,arg2,arg3):
    def wrap(f):
        print("Inside Wrap")
        def wrapped_f(*args):
            print("Inside Wrapped_f()")
            print("decorator arguments",arg1,arg2,arg3)
            f(*args)
        return wrapped_f
    return wrap

@decorator_func_with_arguments("Hello","World",42)
def sayHello(a1,a2,a3,a4):
    print("Inside sayHello:",a1,a2,a3,a4)

