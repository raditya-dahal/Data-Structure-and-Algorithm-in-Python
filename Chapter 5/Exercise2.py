class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        
        current_node = self._root_node
        parent_node = None

        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        new_node = Node(data, parent_node=parent_node)

        if parent_node is None:
            self._root_node = new_node
        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.
        """
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif data < current.data:
                current = current._left_child
            else:
                current = current._right_child
        return None        

    def find_minimum(self):
       
        current = self._root_node
        if current is None:
            return None

        while current._left_child:
            current = current._left_child

        return current

    def find_maximum(self):
       
        current = self._root_node
        if current is None:
            return None

        while current._right_child:
            current = current._right_child

        return current