def find_smallest(xs):
    if not xs:
        raise ValueError("find_smallest() iterable argument is empty")
    smallest = xs[0]
    smallest_idx = 0
    for i in range(1, len(xs)):
        if xs[i] < smallest:
            smallest = xs[i]
            smallest_idx = i
    return smallest_idx


def selection_sort(xs):
    xs = xs[:]
    res = []
    for _ in range(len(xs)):
        smallest = find_smallest(xs)
        res.append(xs.pop(smallest))
    return res
