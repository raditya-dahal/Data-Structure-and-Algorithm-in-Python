from collections import queue

def get_pairs(numbers):
    even_queue = queue()
    odd_queue = queue()
    result = []

    for num in numbers:
        if num % 2 == 0:  # even
            if odd_queue._size > 0:
                odd_num = odd_queue.dequeue()
                result.append((num, odd_num))
            else:
                even_queue.enqueue(num)
        else:  # odd
            if even_queue._size > 0:
                even_num = even_queue.dequeue()
                result.append((even_num, num))
            else:
                odd_queue.enqueue(num)

    return result