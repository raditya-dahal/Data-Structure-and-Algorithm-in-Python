class DoublyListNode:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'<DoublyListNode: {self.data}>'


class DoublyLinkedList:
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current = self._head
        values = ''
        while current:
            values += f', {current.data}'
            current = current.next
        plural = '' if self._size == 1 else 's'
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """Append value to the end of the list"""
        new_node = DoublyListNode(value)

        if self._head is None:
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def insert(self, index, value):
        """Insert value at given index"""
        if index < 0 or index > self._size:
            raise ValueError("Index out of bounds")

        new_node = DoublyListNode(value)

        # Insert at beginning
        if index == 0:
            if self._head is None:
                self._head = self._tail = new_node
            else:
                new_node.next = self._head
                self._head.prev = new_node
                self._head = new_node

        # Insert at end
        elif index == self._size:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

        # Insert in middle
        else:
            current = self._head
            for _ in range(index):
                current = current.next
            prev_node = current.prev

            prev_node.next = new_node
            new_node.prev = prev_node

            new_node.next = current
            current.prev = new_node

        self._size += 1

    def remove(self, index):
        """Remove a node from the position given by index"""
        # Raise ValueError if index is out of bounds (also covers empty list)
        if index < 0 or index >= self._size:
            raise ValueError("Index out of bounds")

        # Locate the node to remove
        current = self._head
        for _ in range(index):
            current = current.next

        # Save value
        value = current.data

        # Update previous node
        if current.prev:
            current.prev.next = current.next
        else:
            # Removing head
            self._head = current.next

        # Update next node
        if current.next:
            current.next.prev = current.prev
        else:
            # Removing tail
            self._tail = current.prev

        # Delete node and update size
        del current
        self._size -= 1

        return value