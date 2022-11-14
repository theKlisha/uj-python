import sys

sym = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

last_n = 0
sum = 0

for n in reversed(sys.argv[1]):
    current_n = sym[n]
    if last_n > current_n:
        sum -= current_n
    else:
        sum += current_n
    last_n = current_n

print(sum)
