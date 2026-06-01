"""
Linked List are linear data structures where the elements
are not stored in contiguous locations and every element
is a separate object with a data part and address part.
The elements are linked using pointers and addresses.
Each element is known as a node. Due to the dynamicity and
ease of insertions and deletions, they are preferred over
the arrays. It also has few disadvantages like the nodes
cannot be accessed directly instead we need to start from
the head and follow through the link to reach to a node we
wish to access.

When a Linked List is suitable:

* Insert items "in between" other items
* Collection size is unknown and/or changes often
* You don't need random access to elements
* Not concerned about the memory usage

Linked List are recursive data structures, because they
* A linked list is empty
* Or it consists of a node that contains a value and a reference to a linked list
"""

class SLLNode:
    """Singly Linked List Node"""
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"SLLNode({self.data})"

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


def test_sll_node():
    """Test SLLNode class"""
    node = SLLNode("apple")
    print(node)
    assert node.get_data() == "apple"
    assert node.get_next() is None

    node.set_data("banana")
    print(node)
    assert node.get_data() == "banana"

    node.set_next(SLLNode("orange"))
    print(node.get_next())
    assert node.get_next().get_data() == "orange"


if __name__ == "__main__":
    test_sll_node()
