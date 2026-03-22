# Binary search

def binary_search(list, item):

    low = 0
    high = len(list) - 1

    while low < high:
        mid = low + high
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

        return None


result = binary_search([1, 2, 3, 5, 6, 7], 7)
print("Binary", result)


# Selection sort is the neat algorithm but it is the so slow.

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# Actual  sorting algorithm


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print("SelectingSort", selectionSort([5, 3, 6, 2, 10]))


def count_down(n):
    print("i", n)
    if n <= 0:
        return
    count_down(n - 1)


count_down(9)


def factorial(n):
    if (n == 1):
        return 1
    else:
        return n * factorial(n - 1)


print("factorial", factorial(5))


def two_sum(nums, target):
    sets = {}
    for i, num in enumerate(nums):
        sub = target - num
        if sub in sets:
            return [sets[sub], i]
        sets[num] = i


res = two_sum([3, 3], 6)
print("res", res)
