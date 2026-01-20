'''
Implementing insert method
Here you have a class named IntArray with an implementation of an Array that can store integer values. It uses another class ReservedMemory (also provided) to store the integer values in memory as bytes (you can convert values to byte type or you can just use integer values between 0 and 255. Both are fine. In the code provided the latter form is used).

When instantiating an IntArray variable, the size of the array elements can be defined. By default this value is 2 bytes, that gives room to store values from -32768 to 32767 (65536 different values in total, i.e. 16 bit range)

Some internal methods and some public methods have been already implemented. Your job is to implement a new method "insert". The definition of the method is already present. Just replace the placeholder code provided with your own code.

This new insert method has to be able to insert a new element at whatever position/index of the array. For that a new array has to be created and the old content has to be copied making room for the new value

You will have to study a little bit the provided code to understand how it works. And you can use the already implemented methods as an example on what can be done.

Notice that ReservedMemory has a copy function you can use to copy the content of an old array to a new one.

For example:
Test	
array = IntArray()
for i in range(6):
    array.append(i)
array.insert(5, 10)
print(array)

Result
IntArray (7 elements): [0, 1, 2, 3, 4, 10, 5]

'''



from __future__ import annotations
import ctypes

class ReservedMemory():
    def __init__(self, size: int) -> None:
        if not isinstance(size, int):
            raise(TypeError('Memory size must be a positive integer > 0!'))
        if not 1 <= size <= 65536:
            raise(ValueError('Reserved memory size must be between 1 and 65536 bytes!'))
        self._reserved_memory = ctypes.create_string_buffer(size)

    def __len__(self) -> int:
        return len(self._reserved_memory)

    def copy(self, mem_source, count=None, source_index=0, destination_index=0) -> None:
        if count is None:
            count = len(mem_source._reserved_memory) - source_index
        self._reserved_memory[destination_index:destination_index+count] = \
            mem_source._reserved_memory[source_index:source_index+count]

    def __getitem__(self, k: int) -> int:
        return ord(self._reserved_memory[k])

    def __setitem__(self, k: int, val: int) -> None:
        self._reserved_memory[k] = val


class IntArray():
    def __init__(self, bytes_per_element: int = 2) -> None:
        self._resmem = None
        self._size = 0
        self._bytes_per_element = bytes_per_element
        self._shift_val = 2 ** ((self._bytes_per_element * 8) - 1)
        self._min_val = -self._shift_val
        self._max_val = self._shift_val - 1

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self) -> int:
        if self._iter_index < self._size:
            self._iter_index += 1
            return self.__getitem__(self._iter_index - 1)
        raise StopIteration

    def __repr__(self) -> str:
        if not self._resmem:
            return "Empty IntArray"
        return f"IntArray ({self._size} elements): [{', '.join(str(v) for v in self)}]"

    def __setitem__(self, k: int, val: int) -> None:
        val_to_store = val + self._shift_val
        for i in range(self._bytes_per_element):
            self._resmem[k * self._bytes_per_element + i] = (val_to_store >> (8 * i)) & 255

    def __getitem__(self, k: int) -> int:
        stored_val = 0
        for i in range(self._bytes_per_element):
            stored_val |= self._resmem[k * self._bytes_per_element + i] << (8 * i)
        return stored_val - self._shift_val

    def append(self, val: int) -> None:
        self._size += 1
        new_mem = ReservedMemory(self._size * self._bytes_per_element)
        if self._resmem:
            new_mem.copy(self._resmem)
        self._resmem = new_mem
        self.__setitem__(self._size - 1, val)

    def pop(self) -> int:
        if self._size == 0:
            return None
        val = self.__getitem__(self._size - 1)
        self._size -= 1
        if self._size > 0:
            new_mem = ReservedMemory(self._size * self._bytes_per_element)
            new_mem.copy(self._resmem, self._size * self._bytes_per_element)
            self._resmem = new_mem
        else:
            self._resmem = None
        return val

    def insert(self, index: int, val: int) -> None:
        if not 0 <= index <= self._size:
            raise IndexError("Index out of bounds")

        self._size += 1
        new_mem = ReservedMemory(self._size * self._bytes_per_element)

        if self._resmem:
            # Copy elements before index
            if index > 0:
                new_mem.copy(self._resmem, index * self._bytes_per_element)

            # Copy elements after index
            if index < self._size - 1:
                new_mem.copy(
                    self._resmem,
                    (self._size - 1 - index) * self._bytes_per_element,
                    index * self._bytes_per_element,
                    (index + 1) * self._bytes_per_element
                )

        self._resmem = new_mem
        self.__setitem__(index, val)