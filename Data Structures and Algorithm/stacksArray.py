# Implementing stacks using lists
class Stacks:
    # Constructor method to implement stacks
    def __init__(self, value):
        self.stack_lst = []
        self.stack_lst.append(value)
        self.height = 1
        self.top = self.stack_lst[self.height - 1]

    # Printing the stack
    def print_stack(self):
        for i in range(len(self.stack_lst) - 1, -1, -1):
            print(self.stack_lst[i], end=" ")

    # Method to push an element in stack
    def push(self, value):
        self.stack_lst.append(value)
        self.height += 1
        self.top = self.stack_lst[self.height - 1]

    # Method to pop an element from stack
    def pop(self):
        if len(self.stack_lst) == 0:
            return None
        else:
            popped_ele = self.stack_lst[self.height - 1]
            self.stack_lst.remove(self.top)
            self.height -= 1
            self.top = self.stack_lst[self.height - 1]
            return popped_ele

    # Method to get the top element of stack
    def top_ele(self):
        if self.height == 0:
            return None
        else:
            return self.top

    # Method to check if the stack is empty
    def is_empty(self):
        if len(self.stack_lst) == 0:
            return True
        else:
            return False

    # Method to get the height of the stack
    def len_stack(self):
        return self.height

