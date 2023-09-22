class Queue:
    def __init__(self):
        # Initialize an empty list to store the queue elements
        self.items = []

    def enqueue(self, item):
        # Add an item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the front item from the queue
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def peek(self):
        # Return the front item from the queue without removing it
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty"

    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.items)

# Example Usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())  # Expected: 1
print(q.dequeue())  # Expected: 1
print(q.size())  # Expected: 2
