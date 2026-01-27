class StackNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<StackNode: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value):
        """Add a value on top of the stack"""
        new_node = StackNode(value, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        """Remove and return the top value of the stack"""
        if self._top is None:
            return None

        value = self._top.data
        temp = self._top
        self._top = self._top.next
        del temp
        self._size -= 1
        return value

    def __repr__(self):
        current = self._top
        values = []
        while current:
            values.append(str(current.data))  # Convert to string for display
            current = current.next
        plural = 'element' if self._size == 1 else 'elements'
        return f"<Stack ({self._size} {plural}): [{', '.join(values)}]>"