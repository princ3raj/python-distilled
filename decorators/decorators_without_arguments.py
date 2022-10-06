class decorator_without_arguments(object):

    def __init__(self,f):
        print("Inside __init__()")
        self.f = f
    

    def __call__(self,*args):
        print("Inside __call__()")
        self.f(*args)
        print("After self.f(*args)")



@decorator_without_arguments
def sayHello(a1,a2,a3,a4):
    print("say Hello arguments",a1,a2,a3,a4)

print("After Decoration")

print("Preparing to call sayHello()")

sayHello("say","hello","arguments","list")

print("After First sayHello() call")

sayHello("a","different","set","of arguments")

print("After second sayHello() Call")

