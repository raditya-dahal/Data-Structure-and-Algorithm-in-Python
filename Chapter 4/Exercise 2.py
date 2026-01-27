# Stack implementation
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


# Function to check brackets balance
def check_balance(text):
    stack = Stack()
    pairs_count = 0

    # Mapping of closing to opening brackets
    matching = {')': '(', ']': '[', '}': '{'}

    for pos, char in enumerate(text):
        if char in "([{":
            stack.push((char, pos))  # store bracket and its position
        elif char in ")]}":
            if stack._top is None:
                # Closing bracket without matching opening
                return f"Match error at position {pos}"
            top_char, top_pos = stack.pop()
            if matching[char] != top_char:
                # Mismatched pair
                return f"Match error at position {pos}"
            pairs_count += 1

    # Check for any unmatched opening brackets
    if stack._top is not None:
        # Find position of first unmatched opening bracket
        current = stack._top
        while current.next is not None:
            current = current.next
        return f"Match error at position {current.data[1]}"

    return f"Ok - {pairs_count}"