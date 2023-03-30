#!/bin/python3

from itertools import product

if __name__ == "__main__":
    k, m = map(int, input().split())
    n = list()

    for _ in range(k):
        n.append(list(map(int, input().split()))[1:])

    f = lambda x: sum(i**2 for i in x) % m
    print(max(map(f, product(*n))))
