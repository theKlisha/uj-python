# podpunkt A) 
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo, 
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo(self, x):
        print("wykonanie foo({}, {})".format(self, x))

    @classmethod
    def class_foo(cls, x):
        print("class_foo({}, {})".format(cls, x))

    @staticmethod
    def static_foo(x):
        print("wykonanie static_foo({})".format(x))

a = A()
a.foo(123) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a,123) # ditto
a.class_foo(123) # class_foo(<class '__main__.A'>, 123)
A.class_foo(123) # ditto
a.static_foo(123) # wykonanie static_foo(123)
A.static_foo(123) # ditto

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod
from re import error

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print(self.r**2 * 3.14)

class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        print(self.a ** 2)

c = Circle(2)
c.area()

s = Square(2)
s.area()

# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez 
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu
class Memo(ABC):
    def __init__(self):
        self.inner = None
        self.history = set()

    @property
    def value(self):
        return self.inner

    @value.setter
    def value(self, newValue):
        if newValue in self.history:
            raise Exception("this value has been set in the past")
        else:
            self.inner = newValue
            self.history.add(newValue)

m = Memo()
m.value = "a"
print(m.value)
m.value = "b"
print(m.value)
m.value = "a"
