class Root:
    def __init__(self,*args,**kwargs):
        print('Root init',self)
        self.accessiblity_variable_gibberish = False
    def shielded_function(self):
        if hasattr(self, 'accessiblity_variable_gibberish'):
            if self.accessiblity_variable_gibberish:
                return "Exposed because accessibility variable existed and was true"
            else:
                return "Hidden because accessibility variable existed and was false"
        else:
            return "Exposed because accessibility variable did not exist"

class A(Root):
    def __init__(self,*args,**kwargs):
        print('A init',self)
        sup = super()
        print(f"super() when called in A init is {sup}. Note that it might see something called C object despite that being deeper down in the hierarchy.")
        sup.__init__()

def create_diamond_pattern(parent,child):
    class B(parent):
        def __init__(self,*args,**kwargs):
            print('B init',self)
            # no call to parent's init here
    class C(child,B):
        def __init__(self,*args,**kwargs):
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
    B,C = create_diamond_pattern(Root,A)
    print(f"The Method Resolution Order for the class C is {[cls.__name__ for cls in C.__mro__]}")
    # c is a an instance of C which is a subclass of A but Root initialization never called so it
    #    but only A initialization part, then using this as an A gives us something to use like a malformed instance of A
    c = C(5,4,6)
    print(f"When call shielded function get {c.shielded_function()}") 
    print("""c is an instance of a subclass of A so it is substitutable for anywhere an A can be used like shielded_function,
    but Root init was never called so accessiblity_variable_gibberish is not defined
    and the code to create_diamond_pattern did not ever use that variable name to explicitly change it""")