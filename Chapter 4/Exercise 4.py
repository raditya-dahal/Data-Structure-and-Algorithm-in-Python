# Node class
class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'


# Queue using ListNode
class Queue:
    def __init__(self):
        self._head = None  # newest element (enqueue here)
        self._tail = None  # oldest element (dequeue from here)
        self._size = 0

    def enqueue(self, value):
        """Add a new element to the left (head)"""
        new_node = ListNode(value)

        if self._head is None:
            # Empty queue
            self._head = self._tail = new_node
        else:
            # Insert at head
            new_node.next = self._head
            self._head = new_node

        self._size += 1

    def dequeue(self):
        """Remove and return the oldest element (tail)"""
        if self._tail is None:
            return None  # empty queue

        # If queue has only one element
        if self._head == self._tail:
            value = self._tail.data
            self._head = self._tail = None
            self._size -= 1
            return value

        # Find the node before the tail
        current = self._head
        while current.next != self._tail:
            current = current.next

        value = self._tail.data
        self._tail = current
        self._tail.next = None
        self._size -= 1
        return value

    def __repr__(self):
        current = self._head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next
        plural = 'element' if self._size == 1 else 'elements'
        return f"<Queue ({self._size} {plural}): [{', '.join(values)}]>"