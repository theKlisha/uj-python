def deep_append(l):
    lists = []

    def traverse(l, d):
        if isinstance(l, list):
            lists.append((l, d))
            for i in l: traverse(i, d + 1)

    traverse(l, 0)
    max_depth = max(lists, key=lambda x: x[1])[1]
    deepest_lists = filter(lambda x: x[1] == max_depth, lists)
    for l in deepest_lists:
        l[0].append(l[0][-1] + 1)

list1 = [1, 2, [3, 4, [5, 6], 5], 3, [4, 5]]
deep_append(list1)
assert(list1 == [1, 2, [3, 4, [5, 6, 7], 5], 3, [4, 5]])

list2 = [1, [2, 3], 4]
deep_append(list2)
assert(list2 == [1, [2, 3, 4], 4])

list3 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
deep_append(list3)
assert(list3 == [3, 4, [2, [1, 2, [7, 8, 9], 3, 4], 3, 4], 5, 6, 7])

list4 = [1, [3], [2]]
deep_append(list4)
assert(list4 == [1, [3, 4], [2, 3]])
