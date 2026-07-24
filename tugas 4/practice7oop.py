from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return 'Queue kosong!'
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        
    def is_empty(self): return len(self.items) == 0
    def size(self): return len(self.items)
    def __str__(self): return str(list(self.items))



q = Queue()
q.enqueue('Andi')
q.enqueue('Budi')
q.enqueue('Citra')

print(q)
['Andi', 'Budi', 'Citra']
print(q.peek())

print(q.dequeue())
print(q)
print(q.size())
print(q.is_empty())
