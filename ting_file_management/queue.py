class Queue:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        dequeued = self.items[0]
        self.items = self.items[1:]

        return dequeued

    def search(self, index):
        if (index < 0 or index > len(self) - 1):
            raise IndexError

        return self.items[index]
