"""Write a method that from a given position find the next free slot of the table
Write a method called _find_free_slot() that accepts a parameter representing a position on the heap (an index) 
and returns the index of the next  free slot available on the hash table. It should take into account that after reaching 
the end of the table during the search, it should continue from the beginning of the table. Also to avoid looping 
infinitely, if the start position is reached again, it should return None
"""
class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'

class HashTable:
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0
    
    def __repr__(self):
        text = ''
        for index, slot in enumerate(self.slots):
            if slot:
                text += f', {index}: {slot}'
        plural = '' if self.used_slots == 1 else 's'
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]>'

    def _hash(self, key):
        return len(key) % self.size

    def _find_free_slot(self, start):
        """
        Finds the next free slot starting from 'start'. Wraps around if necessary.
        Returns None if no free slots exist.
        """
        for i in range(self.size):
            index = (start + i) % self.size
            if self.slots[index] is None:
                return index
        return None