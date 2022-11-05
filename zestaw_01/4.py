import sys

h = int(sys.argv[1])
w = int(sys.argv[2])

def make_row(a, b, n):
    x = a
    for _ in range(0, n):
        x += b + a
    return x + "\n"

grid = make_row("+", "---", w)
for _ in range(0, h):
    grid += make_row("|", "   ", w)
    grid += make_row("+", "---", w)

print(grid)
