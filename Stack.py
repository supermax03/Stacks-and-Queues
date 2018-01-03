class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def put(self, item):
        self.items.append(item)
        self.top += 1

    def peek(self):
        item = None
        if len(self.items) > 0:
            item = self.items[self.top]
        return item

    def empty(self):
        return len(self.items) == 0

    def pop(self):
        item = None
        if len(self.items) > 0:
            item = self.items[self.top]
            self.items = self.items[:self.top]
            self.top -= 1
        return item


if __name__ == '__main__':
    myStack = Stack()
    myStack.put(1)
    myStack.put(2)
    myStack.put(3)
    print myStack.peek()
    print myStack.pop()
    print myStack.pop()
    print myStack.pop()
    print myStack.empty()
    print myStack.pop()
