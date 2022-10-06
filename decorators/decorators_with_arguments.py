class decorators_with_arguments(object):

    def __init__(self,arg1,arg2,arg3):
        print("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
    
    def __call__(self,f):
        print("Inside __call__()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator Arguments:",self.arg1,self.arg2,self.arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f

@decorators_with_arguments("hello","world",42)
def sayHello(a1,a2,a3,a4):
    print("sayHello() arguments:",a1,a2,a3,a4)

print("After Decoration")
print("Preparing to call sayHello()")
sayHello("say","Hello","argument","list")
sayHello("a","different","set of","arguments")