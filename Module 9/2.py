"""
Implement a sift_down function
Given the information you have received about the sift_down function, implement it.

Given an array like: [6, 2, 5, 8, 1], and calling the sift_down function with the parameters "array, start=1, end=4" (sink the node with the value of 1), the array should be modified to look like this: [6, 8, 5, 2, 1]

Remember that the left child on a zero based array is at position: 2*current_node_index+1 and the right child is at: 2*current_node_index+2

Esimerkiksi:

Testi	Tulos
array = [6, 2, 5, 8, 1]
sift_down(array, 1, 4)
print(array)
[6, 8, 5, 2, 1]

"""

def sift_down(array, start, end):
    root = start

    while 2 * root + 1 <= end:  # while root has at least a left child
        child = 2 * root + 1    # left child
        swap = root

        if array[swap] < array[child]:
            swap = child

        if child + 1 <= end and array[swap] < array[child + 1]:
            swap = child + 1    # right child

        if swap == root:
            return
        else:
            array[root], array[swap] = array[swap], array[root]
            root = swap