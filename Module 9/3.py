"""
Implement a heapsort function
Given the information you have received in the course about the heapsort algorithm, implement a sort function that uses it. The function needs only to accept the array to be sorted as parameter. Use the sift_down helper function to complete the task (it is available even if it is not visible)

Given an array like: [6, 8, 5, 1, 2], the sorted array would be: [1, 2, 5, 6, 8]


Vastaus:(rangaistus: 0 %)
"""

def heap_sort(array):
    n = len(array)

    # Build the max heap
    for start in range((n - 2) // 2, -1, -1):
        sift_down(array, start, n - 1)

    # Extract elements from the heap
    for end in range(n - 1, 0, -1):
        array[0], array[end] = array[end], array[0]
        sift_down(array, 0, end - 1)