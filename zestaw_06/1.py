#!/bin/python3

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr = sorted(arr, key=lambda r: r[k])

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()
