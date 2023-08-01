# Q18  Write Python Program to Implement Stack Operations


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        item = self.stack.pop()
        print(f"Popped: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack:", self.stack)


# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.pop()
stack.display()

print("Stack size:", stack.size())
print("Top of stack:", stack.peek())
