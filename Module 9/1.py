"""
Implement an Insertion sort function
Given the information you have received in the course about the Insertion sort algorithm, implement a function that uses it. The function needs only to accept the array to be sorted as parameter. The function returns nothing. The array is sorted in-place.

Given an array like: [6, 8, 5, 1, 2], the sorted array would be: [1, 2, 5, 6, 8]

Esimerkiksi:

Testi	Tulos
array = [6, 8, 5, 1, 2]
insertion_sort(array)
print(array)
[1, 2, 5, 6, 8]

"""
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        
        array[j + 1] = key