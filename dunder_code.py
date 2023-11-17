"""
overwriting
and pylint doesn't even complain
"""

def fun_a(_ : int) -> None:
    """
    nothing
    """
    return

def fun_b(dumb : int) -> int:
    """
    print + identity
    """
    print(dumb)
    return dumb

if __name__ == '__main__':
    print((fun_a))
    fun_a.__code__ = fun_b.__code__
    print(fun_a(1))
