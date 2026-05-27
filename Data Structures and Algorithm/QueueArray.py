# Implementing queues using lists
# Class to implement queues
class Queue:
    # Constructor method for queue
    def __init__(self, value):
        self.queue_lst = []
        self.queue_lst.append(value)
        self.first_index = 0
        self.first = self.queue_lst[self.first_index]

    # Method to print the elements of queue
    def print_queue(self):
        for ele in self.queue_lst:
            print(ele, end=" ")

    # Method to add an element in the queue
    def enqueue(self, value):
        self.queue_lst.append(value)

    # Method to pop an element from the queue
    def dequeue(self):
        if len(self.queue_lst) == 1:
            return None
        popped_ele = self.queue_lst[self.first_index]
        self.queue_lst.remove(self.first)
        self.first = self.queue_lst[self.first_index]
        return popped_ele


q = Queue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
print("Queue: ", end=" ")
q.print_queue()
q.dequeue()
print("\nQueue after removing the first element: ", end=" ")
q.print_queue()