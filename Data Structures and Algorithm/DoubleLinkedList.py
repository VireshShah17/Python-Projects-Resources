# Class to create a node in doubly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# Class to create a doubly linked list
class DoublyLinkedList:
    # Constructor method for list
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Method to print the list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Method to append a node in list
    def append_node(self, value):
        new_node = Node(value)
        # Checking if the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Pointing the tail node to new node
            self.tail.next = new_node
            # Pointing the new node to last node
            new_node.prev = self.tail
            # Updating our tail
            self.tail = new_node
        self.length += 1
        return True

    # Method to pop a node from list
    def pop_node(self):
        if self.length == 0:
            return None
        temp = self.tail.prev
        last = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp.next = None
            self.tail.prev = None
            self.tail = temp
        self.length -= 1
        return last

    # Method to prepend a node in list
    def prepend_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    # Method to pop the first node from list
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp

    # Method to get a node by its index
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    # Method to set value of a particular node
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        else:
            return False

    # Method to insert a node at particular index
    def insert_node(self, index, value):
        # Checking for index out of range
        if index < 0 or index > self.length:
            return False
        # Adding node at first position
        if index == 0:
            return self.prepend_node(value)
        # Adding node at the end
        if index == self.length:
            return self.append_node(value)
        # Inserting somewhere in between
        prev = self.get(index - 1)
        temp = self.get(index)
        new_node = Node(value)
        # Pointing previous node to our new node
        prev.next = new_node
        # Pointing previous pointer to previous node
        new_node.prev = prev
        # Pointing the next pointer to next node
        new_node.next = temp
        temp.prev = new_node
        self.length += 1
        return True

    # Method to remove a particular node
    def remove_node(self, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_node()
        # Deleting node from between
        temp = self.get(index)
        prev = self.get(index - 1)
        temp.prev.next = temp.next
        temp.next.prev = prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return True

