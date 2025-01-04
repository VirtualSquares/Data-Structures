class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]

    def display(self):
        return list(map(int, self.items))

que = Queue()
que.enqueue(3)
que.enqueue(4)
que.enqueue(5)
que.enqueue(6)
que.enqueue(7)
print(que.display())
print(que.dequeue())
print(que.dequeue())
print(que.dequeue())
print(que.peek())
print(que.display())
