"""
A queue has been implemented using two stacks.
"""

# Two stacks used to simulate queue behavior
stack1 = []  # Used for enqueue operations
stack2 = []  # Used for dequeue operations

# Enqueue operation: push the element onto stack1
def enqueue(x):
    stack1.append(x)

# Dequeue operation:
# If stack2 is empty, transfer all elements from stack1 to stack2 (reversing order)
# Then pop from stack2 to simulate queue behavior
def dequeue():
    if not stack1 and not stack2:
        return None  # Queue is empty
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    return stack2.pop()

# Enqueue elements 0 through 9
for i in range(10):
    enqueue(i)

# Dequeue and print all elements (FIFO order)
for i in range(10):
    print(dequeue(), end=",")
