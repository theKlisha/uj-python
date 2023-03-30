from functools import singledispatch, singledispatchmethod

@singledispatch
def add(*args):
    s = 0
    for item in args: s += item
    return s

@add.register
def _(l: list):
    s = 0
    for item in l: s += item
    return s

print(add(1, 2, 3))
print(add([1, 2, 3]))

class Adder:
    @singledispatchmethod
    def add(self, *args):
        s = 0
        for item in args: s += item
        return s

    @add.register
    def _(self, l: list):
        s = 0
        for item in l: s += item
        return s

a = Adder()
print(a.add(1, 2, 3))
print(a.add([1, 2, 3]))
