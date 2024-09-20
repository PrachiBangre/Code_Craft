# Function to insert element at the bottom of the stack
def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
    else:
        # Pop all elements until stack is empty
        temp = stack.pop()
        insert_at_bottom(stack, item)
        # Push all elements back
        stack.append(temp)

# Function to reverse the stack
def reverse_stack(stack):
    if len(stack) > 0:
        # Pop the top element
        temp = stack.pop()
        # Recursively reverse the remaining stack
        reverse_stack(stack)
        # Insert the popped element at the bottom
        insert_at_bottom(stack, temp)

# Example usage
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)