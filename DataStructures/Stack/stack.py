class Stack:
    def __init__(self):
        # Initialize an empty list to store the stack elements
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item from the stack
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        # Return the top item from the stack without removing it
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the stack
        return len(self.items)

# Example Usage:
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())  # Expected: 3
print(s.pop())   # Expected: 3
print(s.size())  # Expected: 2
