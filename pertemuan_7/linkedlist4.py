class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head,data):
    new_node = Node(data)
    new_node.next = head
    return new_node
    
head =  Node("B")
head = insert_at_beginning(head,"A")

def print_linked_list(head):
    while head:
        print(f"[{head.data}] -->",end="")
        head = head.next
        print("NULL")

print_linked_list(head)
