class DLLNode:
    """Doubly Linked List Node"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
    
    def __repr__(self):
        return f"DLLNode({self.data})"

    def get_data(self):
        """Return the data of the node"""
        return self.data

    def set_data(self, new_data):
        """Replace the existing data of the node"""
        self.data = new_data

    def get_next(self):
        """Return the next node"""
        return self.next

    def set_next(self, next_node):
        """Set the next node"""
        self.next = next_node
    
    def get_previous(self):
        """Return the previous node"""
        return self.previous
    
    def set_previous(self, previous_node):
        """Set the previous node"""
        self.previous = previous_node


def test_dll_node():
    """Test DLLNode class"""
    node = DLLNode("apple")
    print(node)
    assert node.get_data() == "apple"
    assert node.get_next() is None
    assert node.get_previous() is None

    node.set_data("banana")
    print(node)
    assert node.get_data() == "banana"

    node.set_next(DLLNode("orange"))
    print(f"next: {node.get_next()}")
    assert node.get_next().get_data() == "orange"

    node.set_previous(DLLNode("pear"))
    print(f"previous: {node.get_previous()}")
    assert node.get_previous().get_data() == "pear"


if __name__ == "__main__":
    test_dll_node()
