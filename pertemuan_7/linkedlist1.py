class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

a = Node("A")
b = Node("B")
c = Node("C")

a.next = b
b.next = c

current = a
while current:
    print(current.data)
    current = current.next
    