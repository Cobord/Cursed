"""
https://www.hillelwayne.com/negatypes/
"""
# pylint:disable = too-few-public-methods,invalid-name

from abc import ABC
from functools import singledispatch

class NotIterable(ABC):
    """
    does not have a dunder iter
    """

    @classmethod
    def __subclasshook__(cls, C):
        """
        does not have a dunder iter
        """
        return not hasattr(C, "__iter__")
class IterableNotString(ABC):
    """
    does not have a dunder iter and is not a string
    """

    @classmethod
    def __subclasshook__(cls, C):
        """
        does not have a dunder iter and is not a string
        """
        return hasattr(C, "__iter__") and not C==type("a")
class Iterable(ABC):
    """
    does have a dunder iter
    """

    @classmethod
    def __subclasshook__(cls, C):
        """
        does have a dunder iter
        """
        return hasattr(C, "__iter__")
class NotCallable(ABC):
    """
    does not have a dunder call
    """

    @classmethod
    def __subclasshook__(cls, C):
        """
        does not have a dunder call
        """
        return not hasattr(C, "__call__")
class Callable(ABC):
    """
    does have a dunder call
    """

    @classmethod
    def __subclasshook__(cls, C):
        """
        does have a dunder call
        """
        return hasattr(C, "__call__")

@singledispatch
def fun_testing(_arg):
    """
    runs if the below don't work
    """
    print("Generic Version")

@fun_testing.register(Callable)
def _(arg : Callable):
    """
    how to run on Callable
    """
    print(f"{arg} is callable")
@fun_testing.register(NotIterable)
def _(arg : NotIterable):
    """
    how to run on NotIterable
    """
    print(f"{arg} is not iterable")
@fun_testing.register(Iterable)
def _(arg : Iterable):
    """
    how to run on Iterable
    """
    print(f"{arg} is iterable including string")
# if uncomment this, then because of this and above both get an ambiguous dispatch RuntimeError
# when trying to do fun_testing on [1,2,3] which satisfies both subclasshook's
# @fun_testing.register(IterableNotString)
# def _(arg : IterableNotString):
#    print(f"{arg} is iterable, but not a string")

# false positive of hasattr(type(4),'__call__'), callable(4) does not give such a false positive
fun_testing(4)
print(f"But callable(4) says {callable(4)}")
fun_testing([1,2,3])
fun_testing("hello")
fun_testing(lambda y: y)
