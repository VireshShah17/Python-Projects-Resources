# Class to create a node to implement stack using linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Class to implement stack
class Stack:
    # Stack constructor method
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    # Method to print items of stack
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next

    # Method to push an element in stack
    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    # Method to pop an item from a stack
    def pop(self):
        if self.top is None:
            return None
        temp = self.top.next
        self.top.next = None
        self.top = temp
        self.height -= 1
        return temp

    # Method to access the top-most element of stack
    def top_element(self):
        if self.top is None:
            return None
        else:
            return self.top.value

    # Method to check is our stack is empty or not
    def is_empty(self):
        if self.height == 0:
            return True
        else:
            return False

    # Method to get the number of elements in stack
    def len_stack(self):
        if self.height == 0:
            return None
        else:
            return self.height



stk = Stack(5)
# Pushing elements to the stack
stk.push(6)
stk.push(7)
stk.push(8)
print("Stack: ", end=" ")
stk.print_stack()
stk.pop()
print("\nStack after popping the topmost element: ", end=" ")
stk.print_stack()
print("\nHeight of Stack: ", stk.len_stack())