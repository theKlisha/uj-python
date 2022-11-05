size = int(input("input size of the triangle: "))

for x in range(0, (size + 1) // 2):
    left = x
    right = size - x - 1
    l = ["*" if i == left or i == right or x == 0 else " " for i in range(0, size)]
    print("".join(l))
