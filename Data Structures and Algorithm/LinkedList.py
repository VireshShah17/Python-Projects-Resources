# Class to create a node for linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Class to create a linked list
class LinkedList:
    # Constructor method for linked list
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Method to print the linked list
    def print_linked_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Method to append a node
    def append_node(self, value):
        new_node = Node(value)
        # Checking if the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # Method to pop a node from linked list
    def pop_node(self):
        # Checking if the list is empty
        if self.head is None:
            return None
        # Checking if the list has a single element
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp =  self.head
            pre = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return temp

    # Method to prepend a node in linked list
    def prepend_node(self, value):
        new_node = Node(value)
        # Checking if the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # Method to pop the first node from the linked list
    def pop_first(self):
        if self.head is None:
            print("Can't perform this operation cause the Linked list is empty!")
        # Checking if the list has a single element
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return temp

    # Method to get an element from particular index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    # Method to set a value for a particular node
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        else:
            return False

    # Method to insert a node at particular index
    def insert_node(self, index, value):
        # Checking if index is out of bound
        if index < 0 or index > self.length:
            return False
        # Inserting at first position
        if index == 0:
            return self.prepend_node(value)
        # Inserting at last position
        if index == self.length:
            return self.append_node(value)
        # Inserting somewhere in between the list
        temp = self.get(index - 1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    # Method to remove a node
    def remove_node(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_node()
        prev = self.get(index - 1)
        temp = self.get(index)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    # Method to reverse the linked list
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

