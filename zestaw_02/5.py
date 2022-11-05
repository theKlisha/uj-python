def funn(n):
    max_gap = 0
    while n != 0 and n & 1 == 0:
        n = n >> 1
    while n != 0:
        while n & 1 == 1:
            n = n >> 1
        gap = 0
        while n != 0 and n & 1 == 0:
            gap += 1
            n = n >> 1
        max_gap = max(gap, max_gap)
    return max_gap

assert(funn(9) == 2)
assert(funn(15) == 0)
assert(funn(20) == 1)
assert(funn(529) == 4)
assert(funn(1041) == 5)
