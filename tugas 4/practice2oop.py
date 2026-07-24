class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return 'stack kosong!'
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return 'stack kosong!'
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
        
    def __str__(self):
        return str(self.items)
    

if __name__ == "__main__":
    S = Stack()

    S.push(10)
    S.push(20)
    S.push(30)

    print(S)
    print(S.peek())
    print(S.pop())
    print(S)
    print(S.size())
    print(S.is_empty())
    