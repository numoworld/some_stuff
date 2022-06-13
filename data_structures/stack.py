class Stack:
    def __init__(self):
        self.stack = []

    def add(self, value):
        if value not in self.stack:
            self.stack.append(value)
            return True
        else:
            return False

    def peek(self):
        if len(self.stack) <= 0:
            raise Exception('Stack is empty')
        return self.stack[-1]

    def remove(self):
        if len(self.stack) <= 0:
            raise Exception('Stack is empty')
        else:
            return self.stack.pop()

if __name__ == '__main__':
    stack = Stack()
    stack.add(100)
    stack.add(20)
    stack.add(30)
    print(stack.peek())
    stack.remove()
    print(stack.peek())