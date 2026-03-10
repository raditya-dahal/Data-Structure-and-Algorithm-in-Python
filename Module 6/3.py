"""
Write a get method with alternative value

For example:

Test	Result
h=HashTable()

h.put('Name', 'HashTable')
print(h.get('Name'))
HashTable
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
        return sum((index+1) * ord(char) * ord(char) for index, char in enumerate(key)) % self.size

    def _find_free_slot(self, start):
        current = start
        while self.slots[current]:
            current = (current + 1) % self.size
            if current == start:
                return None
        return current

    def _find_key(self, start, key):
        current = start
        while self.slots[current] and self.slots[current].key != key:
            current = (current + 1) % self.size
            if current == start:
                return None
        if self.slots[current]:
            return current
        return None

    def put(self, key, value):
        if self.used_slots == self.size:
            raise MemoryError('Hash table is full')
        h = self._hash(key)
        key_index = self._find_key(h, key)
        if key_index is not None:
            self.slots[key_index].value = value
        else:
            free_index = self._find_free_slot(h)
            if free_index is None:
                raise MemoryError('Hash table is full')
            self.slots[free_index] = HashItem(key, value)
            self.used_slots += 1

    def get(self, key, alternative=None):
        """
        Get the value of 'key'. Returns 'alternative' if key is not found.
        """
        start_index = self._hash(key)
        key_index = self._find_key(start_index, key)
        if key_index is not None:
            return self.slots[key_index].value
        return alternative