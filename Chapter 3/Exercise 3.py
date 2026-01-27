class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size


    def append(self, value):
        """
        Append a value to the end of the list
        """
        new_node = ListNode(value)

        if self._head is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        
        self._size += 1


    def pop(self):
        """
        Removes the last node of the list
        """

        if not self._size:
            return None
        
        # Locate previous node
        if self._size == 1:
            previous_node = None
        else:
            previous_node = self._head
            for _ in range(self._size - 2):
                previous_node = previous_node.next

        # Update head if needed
        if self._head == self._tail:
            self._head = None

        # Save value
        value = self._tail.data
        del self._tail

        # Update tail
        self._tail = previous_node

        if self._tail:
            self._tail.next = None

        self._size -= 1
        return value


    def insert(self, index, value):
        """
        Insert a new node with value in the position given by the index
        """

        if index < 0 or index > self._size:
            raise(ValueError('Index out of bounds'))

        previous_node = None
        next_node = self._head

        for _ in range(index):
            previous_node = next_node
            next_node = next_node.next

        new_node = ListNode(value, next_node)

        if previous_node is None:
            self._head = new_node
        else:
            previous_node.next = new_node
        
        if previous_node == self._tail:
            self._tail = new_node

        self._size += 1


    def remove(self, index):
        """
        Remove a node from the position given by the index
        """

        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))

        previous_node = None
        current_node = self._head

        for _ in range(index):
            previous_node = current_node
            current_node = current_node.next

        value = current_node.data

        # Remove head
        if previous_node is None:
            self._head = current_node.next
        else:
            previous_node.next = current_node.next

        # Remove tail
        if current_node == self._tail:
            self._tail = previous_node

        del current_node

        self._size -= 1

        return value