from inspect import stack


class StackBasedQueue:
    def __init__(self):
        self._InboundStack = stack()
        self._OutboundStack = stack()
        self._size = 0

    def enqueue(self, value):
        """Add an element to the queue"""
        self._InboundStack.push(value)
        self._size += 1

    def dequeue(self):
        """Remove and return the first element from the queue"""
        if self._OutboundStack._top is None:
            # Transfer all elements from Inbound to Outbound if Outbound is empty
            while self._InboundStack._top is not None:
                self._OutboundStack.push(self._InboundStack.pop())

        if self._OutboundStack._top is None:
            return None

        self._size -= 1
        return self._OutboundStack.pop()

    def __repr__(self):
        # Correct display from front to back
        front_list = []
        # OutboundStack: top is front-most
        current = self._OutboundStack._top
        temp = []
        while current:
            temp.append(str(current.data))
            current = current.next
        front_list.extend(temp[::-1])  # reverse to show front first

        # InboundStack: top is back-most
        current = self._InboundStack._top
        temp = []
        while current:
            temp.append(str(current.data))
            current = current.next
        front_list.extend(temp)  # already in correct order

        plural = 'element' if self._size == 1 else 'elements'
        return f"<StackBasedQueue ({self._size} {plural}): [{', '.join(front_list)}]>"