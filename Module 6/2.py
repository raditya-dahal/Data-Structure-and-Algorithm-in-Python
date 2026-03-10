"""Write a method that add or updates a key with a value
You have to complete the put() method of a HashTable class that is already given to you. The put method should accept 
two parameters: a key value and a data value. The data value is found through the key value. The method returns nothing.

The method should return MemoryError if the HastTable is full. The method will try to find the key, if it's found, it 
will update its value. If it is not found, it will add the key and data values to the HashTable as a HashItem, being
 careful with not overwriting any other HashItem. It would also update the used_slots counter."""

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
        else:
            return None

    def put(self, key, value):
        """
        Add or update a key with a value in the hash table
        """
        # Compute the initial hash index
        start_index = self._hash(key)

        # Check if the key already exists
        key_index = self._find_key(start_index, key)
        if key_index is not None:
            # Key exists → update value
            self.slots[key_index].value = value
            return

        # Key not found → find a free slot to insert
        free_index = self._find_free_slot(start_index)
        if free_index is None:
            # Table is full
            raise MemoryError("HashTable is full")
        
        # Insert new key-value pair
        self.slots[free_index] = HashItem(key, value)
        self.used_slots += 1