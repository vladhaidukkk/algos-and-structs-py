def binary_search(xs, target):
    low = 0
    high = len(xs) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = xs[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return None
