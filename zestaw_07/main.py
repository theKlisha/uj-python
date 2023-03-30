from share import mesure, animate

def insertionsort(v):
    i = 1
    while (i < len(v)):
        j = i
        while ((j > 0) and (v[j-1] > v[j])):
            v[j], v[j - 1] = v[j - 1], v[j]
            j -= 1
        i += 1

def bubblesort(v):
    for k in reversed(range(0, len(v))):
        for i in range(0, k):
            if (v[i] > v[i + 1]):
                v[i], v[i + 1] = v[i + 1], v[i]

def shellsort(v):
    def shellInner(left, right):
        h = 1
        while h <= (right - left) // 9:
            h = 3 * h + 1

        while h > 0:
            for i in range(left + h, right + 1):
                j = i
                item = v[i]
                while j >= left + h and item < v[j - h]:
                    v[j] = v[j - h]
                    j = j - h
                v[j] = item
            h = h // 3

    shellInner(0, len(v) - 1)

def mergesort(v):
    def merge(left, middle, right):
        T = [None] * (right - left + 1)
        left1 = left
        right1 = middle
        left2 = middle + 1
        right2 = right
        i = 0
        while left1 <= right1 and left2 <= right2:
            if v[left1] <= v[left2]:
                T[i] = v[left1]
                left1 += 1
            else:
                T[i] = v[left2]
                left2 += 1
            i += 1
        while left1 <= right1:
            T[i] = v[left1]
            left1 += 1
            i += 1
        while left2 <= right2:
            T[i] = v[left2]
            left2 += 1
            i += 1
        for i in range(right - left +1):
            v[left + i] = T[i]

    def innerMergesort(left, right):
        if left < right:
            middle = (left + right) // 2
            innerMergesort(left, middle)
            innerMergesort(middle + 1, right)
            merge(left, middle, right)

    innerMergesort(0, len(v) - 1)

def quicksort(v):
    def swap(l, r):
        v[l], v[r] = v[r], v[l]

    def innerQuicksort(left, right):
        if left >= right:
            return
        swap(left, (left + right) // 2)
        pivot = left
        for i in range(left + 1, right + 1):
            if v[i] < v[left]:
                pivot += 1
                swap(pivot, i)
        swap(left, pivot)
        innerQuicksort(left, pivot - 1)
        innerQuicksort(pivot + 1, right)
    
    innerQuicksort(0, len(v) - 1)

sortFunctions = [
    insertionsort,
    bubblesort,
    shellsort,
    mergesort,
    quicksort,
]

file = open("results.txt", "w")

for func in sortFunctions:
    file.write("{}\n".format(func.__name__))
    def m(opt):
        mesurement = mesure(func, 50, opt)
        file.write("{}: Tablica posortowana w czasie {} ms. Liczba operacji: {}\n".format(opt, mesurement["time"] * 1000, mesurement["steps"]))
        return mesurement
    mesurement_R = m("R")
    mesurement_S = m("S")
    mesurement_A = m("A")
    mesurement_T = m("T")
    file.write("\n")
    animate(mesurement_R["history"], mesurement_R["algorytm"])

file.close()
