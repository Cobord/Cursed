"""
https://www.reddit.com/r/Python/comments/tceagd/better_oop_in_python_no_self_needed_anymore/
"""

# pylint:disable = missing-class-docstring,missing-function-docstring,invalid-name
# pylint:disable = attribute-defined-outside-init,no-method-argument
# mypy: ignore-errors

import types

class ClassNamespace(types.SimpleNamespace):
    def __init__(self,superclass,name):
        for k,v in superclass.__dict__.items():
            self.__dict__.update({k:v})
        self.class_name = name
    def __repr__(self):
        items = (f"{k}={v!r}" for k, v in self.__dict__['fields'].items())
        itemstr = ",".join(items)
        return f"Instance of {self.class_name} with fields {itemstr}"
    def my_fields(self):
        return self.__dict__['fields']
    def empty():
        empty_class = ClassNamespace(types.SimpleNamespace(),"Object")
        empty_class.__dict__.update({'fields':{}})
        return empty_class

def Counter(superclass=ClassNamespace.empty()):
    obj = ClassNamespace(superclass,"Counter")
    fields = obj.my_fields()
    fields.update({'value':0})
    def incrValue(qt=1):
        nonlocal fields
        fields['value'] += qt
    def decrValue(qt=1):
        nonlocal fields
        fields['value'] -= qt
    def conditionedIncr(qt=1):
        nonlocal fields
        if fields.get('flag',True):
            incrValue(qt)
        else:
            decrValue(qt)
    def getValue():
        nonlocal fields
        return fields['value']
    obj.incrValue = incrValue
    obj.decrValue = decrValue
    obj.getValue = getValue
    obj.conditionedIncr = conditionedIncr
    return obj

def Flagger(superclass=ClassNamespace.empty()):
    obj = ClassNamespace(superclass,"Flagger")
    fields = obj.my_fields()
    fields.update({'flag':False})
    def toggle():
        nonlocal fields
        fields['flag'] = not fields['flag']
    def getFlag():
        nonlocal fields
        return fields['flag']
    obj.toggle = toggle
    obj.getFlag = getFlag
    return obj

def do_twice(func,*args):
    func(*args)
    func(*args)

c = Counter()
c.incrValue()
c.incrValue(3)
c2 = Counter()
do_twice(c2.decrValue,2)
print(c.getValue(),c2.getValue())
print(c)
print(c2)

f = Flagger(c)
print(f.getFlag(),f.getValue())
f.toggle()
print(f.getFlag(),f.getValue())
f.incrValue()
print(f.getFlag(),f.getValue())
f.conditionedIncr()
print(f.getFlag(),f.getValue())
print(f)
f2 = Flagger(f)
print(f2)
