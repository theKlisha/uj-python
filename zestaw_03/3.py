def odwracanie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left +=1
        right -= 1

l = [1, 2, 3, 4, 5, 6]
odwracanie(l, 1, 3)
print(l)
