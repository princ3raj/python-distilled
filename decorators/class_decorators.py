# class my_decorator(object):

#     def __init__(self,f):
#         print("Inside my_decorator.__init__()")
    
#     def __call__(self):
#         print("inside my_decorator.__call__()")


# @my_decorator
# def aFunction():
#     print("Inside aFunction()")



class entry_exit(object):
    
    def __init__(self,f):
        self.f = f
    
    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited",self.f.__name__)

@entry_exit
def func1():
    return 2


@entry_exit
def func2():
    print("inside func2()")

print(func1())
func2()