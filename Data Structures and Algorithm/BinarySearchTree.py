# Implementing Binary search Tree
# Class to create a node of our tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Class to implement Binary Search Tree
class BinarySearchTree:
    # Constructor method for binary search tree
    def __init__(self):
        self.root = None

    # Method to insert a node in binary search tree
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # Method to check if the tree contains a node
    def contains(self, key):
        temp = self.root
        while temp is not None:
            if temp.value == key:
                return True
            elif temp.value < key:
                temp = temp.right
            else:
                temp = temp.left
        return False

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.contains(27), my_tree.contains(17))