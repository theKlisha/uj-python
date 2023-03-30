#!/bin/python3

if __name__ == '__main__':
    lower = []
    upper = []
    digitOdd = []
    digitEven = []
    for c in input():
        if c.islower():
            lower.append(c)
        elif c.isupper():
            upper.append(c)
        elif c.isdigit():
            if int(c) % 2 == 0:
                digitEven.append(c)
            else:
                digitOdd.append(c)
    arr = sorted(lower) + sorted(upper) + sorted(digitOdd) + sorted(digitEven)
    print("".join(arr))
