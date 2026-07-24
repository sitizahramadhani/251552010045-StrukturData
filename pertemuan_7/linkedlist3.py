class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def print_linked_list(node):
    while node:
        next_id = id(node.next) if node.next else None
        print(f"[{node.next}|{next_id}] -->",end="")
        node = node.next
    print("NULL")

a = Node("A")
b = Node("B")
c = Node("C")

a.next = b  
b.next = c

print_linked_list(a)
