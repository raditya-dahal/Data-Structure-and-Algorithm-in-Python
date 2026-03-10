import random
import time

data = [random.randint(1, 400) for i in range(300)]

# Copy datasets so each algorithm sorts the same data
data_merge = data.copy()
data_quick = data.copy()
data_insertion = data.copy()


# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# Measure Merge Sort time
start = time.time()
merge_sort(data_merge)
end = time.time()
print("Merge Sort Time:", end - start)
print("Sorted Data (Merge):", data_merge)


# Measure Quick Sort time
start = time.time()
data_quick = quick_sort(data_quick)
end = time.time()
print("\nQuick Sort Time:", end - start)
print("Sorted Data (Quick):", data_quick)


# Measure Insertion Sort time
start = time.time()
insertion_sort(data_insertion)
end = time.time()
print("\nInsertion Sort Time:", end - start)
print("Sorted Data (Insertion):", data_insertion)