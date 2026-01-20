'''
Implementing remove method
Continuing last exercise's example, you have now to implement a remove method for the IntArray class.

Again, the IntArray and ReservedMemory classes are provided and you only have to add your own code for the remove method. The method is also already defined.

The remove method should allow to remove any element from the array given its index. It should raise an IndexError if the index provided is not between the bounds of the array. The method returns the value of the removed element or None if the array is empty



For example:

Test    
array = IntArray()
for i in range(6):
    array.append(i)
array.remove(2)
print(array)

Result
    3 IntArray (5 elements): [0, 1, 3, 4, 5]

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

    def remove(self, index: int) -> int:
        if self._size == 0:
            return None

        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")

        val = self.__getitem__(index)
        self._size -= 1

        if self._size == 0:
            self._resmem = None
            return val

        new_mem = ReservedMemory(self._size * self._bytes_per_element)

        if index > 0:
            new_mem.copy(self._resmem, index * self._bytes_per_element)

        if index < self._size:
            new_mem.copy(
                self._resmem,
                (self._size - index) * self._bytes_per_element,
                (index + 1) * self._bytes_per_element,
                index * self._bytes_per_element
            )

        self._resmem = new_mem
        return val