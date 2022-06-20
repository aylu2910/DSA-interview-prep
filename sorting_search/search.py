def binarySearch(array, target):
    # Write your code here.
    i = 0
    while (i < len(array)-1) & (array[i] <= target):
        if target == array[i]:
            return i
        i = i + 1

    return - 1


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
target_notFound = 60
print(binarySearch(array, target))
print(binarySearch(array, target_notFound))
