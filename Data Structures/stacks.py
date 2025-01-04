class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

    def push(self, value):
        self.items.append(value)

    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]

    def display(self):
        return list(map(int, self.items))

stack=Stack()
stack.push('3')
stack.push('17')
stack.push('23')
stack.push('34')
stack.push('18')
stack.push('67')
stack.push('11')
stack.push('10')
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.display())
