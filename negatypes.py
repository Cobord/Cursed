# https://www.hillelwayne.com/negatypes/

from abc import ABC

class NotIterable(ABC):
    
    @classmethod
    def __subclasshook__(cls, C):
        return not hasattr(C, "__iter__")
class IterableNotString(ABC):
    
    @classmethod
    def __subclasshook__(cls, C):
        return hasattr(C, "__iter__") and not C==type("a")
class Iterable(ABC):
    
    @classmethod
    def __subclasshook__(cls, C):
        return hasattr(C, "__iter__")
class NotCallable(ABC):
    
    @classmethod
    def __subclasshook__(cls, C):
        return not hasattr(C, "__call__")
class Callable(ABC):
    
    @classmethod
    def __subclasshook__(cls, C):
        return hasattr(C, "__call__")

from functools import singledispatch
@singledispatch
def fun_testing(arg):
    print("Generic Version")

@fun_testing.register(Callable)
def _(arg : Callable):
    print(f"{arg} is callable")
@fun_testing.register(NotIterable)
def _(arg : NotIterable):
    print(f"{arg} is not iterable")
@fun_testing.register(Iterable)
def _(arg : Iterable):
    print(f"{arg} is iterable including string")
# if uncomment this, then because of this and above both get an ambiguous dispatch RuntimeError
# when trying to do fun_testing on [1,2,3] which satisfies both subclasshook's
# @fun_testing.register(IterableNotString)
# def _(arg : IterableNotString):
#    print(f"{arg} is iterable, but not a string")

x = 4
# false positive of hasattr(type(4),'__call__'), callable(4) does not give such a false positive
fun_testing(x)
x = [1,2,3]
fun_testing(x)
x = "hello"
fun_testing(x)
x = lambda y: y
fun_testing(x)