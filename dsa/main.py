def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while (low <= high):
        mid = (low + high)
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1


result = binary_search([1, 2, 3, 5, 6, 7], 97)
print("Binary", result)
