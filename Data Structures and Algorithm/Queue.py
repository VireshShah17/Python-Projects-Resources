# Implementing queue data structure using linked list
# Class to create node for our queue element
class Node:
    def __init__(self, value):
        self.value = value
        self.next =  None


# Class to implement queue
class Queue:
    # Queue constructor method
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    # Method to print the elements of queue
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Method to add an element in queue
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    # Method to delete an element from queue
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    # Method to return the first element of the queue
    def first_element(self):
        return self.first.value

    # Method to check if the queue is empty or not
    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False

    # Method to get length of our queue
    def len_queue(self):
        return self.length

