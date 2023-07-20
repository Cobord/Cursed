"""
MRO weirdness
"""

# pylint:disable=invalid-name,too-few-public-methods,redefined-outer-name

class Root:
    """
    The top of the diamond
    """
    def __init__(self,*_args,**_kwargs):
        """
        should expect this to be called because it does the initialization
        for Root's and every subclass is one so the general initialization
        would be expected to happen
        """
        print('Root init',self)
        self.accessiblity_variable_gibberish = False
    def shielded_function(self):
        """
        some function which depending on accessiblity_variable_gibberish
        might expose something private
        """
        if hasattr(self, 'accessiblity_variable_gibberish'):
            if self.accessiblity_variable_gibberish:
                return "Exposed because accessibility variable existed and was true"
            return "Hidden because accessibility variable existed and was false"
        return "Exposed because accessibility variable did not exist"

class A(Root):
    """
    one subclass of Root
    """
    def __init__(self,*_args,**_kwargs):
        """
        A init uses super()'s init
        the kind of pattern you would expect if single inheritance tree
        """
        print('A init',self)
        sup = super()
        print("".join([f"super() when called in A init is {sup}.\n",
              "\tNote that it might see something called C object "
              "despite that being deeper down in the hierarchy."]))
        sup.__init__()

def create_diamond_pattern(parent,child):
    """
    make a diamond pattern provided two classes
    with the other child and the bottom class which is the grandchild in 2 ways
    if one relied on Root's initialization to make A instances well formed,
    then we can use this maliciously to make purposefully instances of C
    that we can use as malformed instances of A
    we don't even know the specific details of how it becomes malformed
    in this case we have no use of accessiblity_variable_gibberish anywhere
    in this creation of these two subclasses
    """
    class B(parent):
        """
        the other child
        """
        def __init__(self,*_args,**_kwargs):
            """
            no call to parent's init here
            """
            print('B init',self)
    class C(child,B):
        """
        the incestuous grandchild
        """
        def __init__(self,*args,**kwargs):
            """
            looks normal like A's calling the super's
            """
            print('C init',self)
            sup = super()
            print(f"super() when called in C init is {sup}")
            sup.__init__(args,kwargs)
    return [B,C]

if __name__ == '__main__':
    print("intended behavior with no sibling injected")
    a = A(5,4,6)
    print(f"When call shielded function get {a.shielded_function()}")
    print()
    print("inject a diamond pattern")
    BCreated,CCreated = create_diamond_pattern(Root,A)
    print(f"""The Method Resolution Order for the class C is
          {[cls.__name__ for cls in CCreated.__mro__]}""")
    # c is a an instance of CCreated which is a subclass of A
    #   but Root initialization never called so it
    #   but only A initialization part, then using this as an A
    #   gives us something to use like a malformed instance of A
    c = CCreated(5,4,6)
    print(f"When call shielded function get {c.shielded_function()}")
    print("".join(["c is an instance of a subclass of A so it is substitutable "
          "for anywhere an A can be used like shielded_function\n",
          "\tBut Root init was never called ",
          "so accessiblity_variable_gibberish is not defined\n",
          "\tThe code to create_diamond_pattern did not ever use",
          "that variable name to explicitly change it"]))
