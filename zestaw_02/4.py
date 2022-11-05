a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
n = int(input("n = "))

l = [[x, y, z] for x in range(0, a) for y in range(0, b) for z in range(0, c) if x + y + z != n]

print(l)
