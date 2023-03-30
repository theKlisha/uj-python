from math import hypot, atan2, sin, cos, sqrt

class Zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def conjugate(self):
        return self.__class__(self.r, -self.i)

    def argz(self):
        return atan2(self.i, self.r)

    def __abs__(self):
        return hypot(self.r, self.i)

    def __repr__(self):
        return "Zespolona({}, {})".format(self.r, self.i)

    def __str__(self):
        return "({}{:+}j)".format(self.r, self.i)

    def __add__(self, other):
        o = other if isinstance(other, self.__class__) else Zespolona(other, 0)
        return Zespolona(self.r + o.r, self.i + o.i)

    def __sub__(self, other):
        o = other if isinstance(other, Zespolona) else Zespolona(other, 0)
        return Zespolona(self.r - o.r, self.i - o.i)

    def __mul__(self, other):
        o = other if isinstance(other, Zespolona) else Zespolona(other, 0)
        return Zespolona((self.r * o.r) - (self.i * o.i), (self.r * o.i) + (self.i * o.r))

    def __radd__(self, other):
        return other + self

    def __rmul__(self, other):
        return self * other

    def __rsub__(self, other):
        o = other if isinstance(other, Zespolona) else Zespolona(other, 0)
        return Zespolona(o.r - self.r, o.i - self.i)

    def __eq__(self, other):
        return self.r == other.r and self.i == other.i

    def __ne__(self, other):
        return self.r != other.r or self.i != other.i

    def __pow__(self, other):
        r = abs(self) ** other
        th = self.argz()
        return self.__class__(r * cos(other * th), r * sin(other * th))


def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a ==  b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a ** 2)
    print(b ** 4)


if __name__ == "__main__":
    main()


# Liczby zespolone
# (2+5j)
# (1-3j)
# <class '__main__.Zespolona'> 1 -3
# (3+2j)
# (1+8j)
# (6+5j)
# (5-5j)
# (8+20j)
# (-8-20j)
# True
# False
# True
# False
# (-21+20j)
# (28+96j)
