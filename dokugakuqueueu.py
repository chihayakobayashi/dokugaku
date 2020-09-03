class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        return self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

queue = Queue()
print(queue.is_empty())
queue.enqueue(1)
print(queue.size())
print(queue.is_empty())

for i in range (2,6):
    queue.enqueue(i)
    print(queue.size())

print(queue.items)





