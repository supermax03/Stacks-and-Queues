class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def empty(self):
        return len(self.items) == 0

    def dequeue(self):
        item = None
        if not self.empty():
            item = self.items[0]
            self.items = self.items[1:]
        return item


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print q.dequeue()
    print q.dequeue()
    print q.empty()
    print q.dequeue()
