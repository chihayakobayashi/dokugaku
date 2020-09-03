class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

#問一
stack = Stack()

for w in "yesterday":
    stack.push(w)

reverse = ""
length = stack.size()
for i in range(int(length)):
    item = stack.pop()
    reverse += item

print(reverse)

#問二
stack2 = Stack()

newlist = []
for i in range (1,6):
    stack2.push(i)

length2 = stack2.size()
for i in range(length2):
    item2 = stack2.pop()
    newlist.append(item2)

print(newlist)

    
    
