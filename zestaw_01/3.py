import sys

l = int(sys.argv[1])
top = "|"
bottom = "0"

for x in range(0, l): 
    top += "....|"
    bottom += str(x + 1).rjust(5)

print(top + "\n" + bottom)
