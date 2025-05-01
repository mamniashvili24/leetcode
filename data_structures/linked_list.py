from model.node import node

class linked_list:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_first(self, value):
        new_node = node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_last(self, value):
        new_node = node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_first(self):
        if not self.head:
            print('cant delete it is empty')
            return
        
        self.head = self.head.next
        if not self.head:
            self.tail = None

    def remove_last(self):
        if not self.head:
            print('cant delete it is empty')
            return
        
        if not self.head.next:
            self.head = None
            self.tail = None
            return

        current = self.head
        while current.next is not self.tail:
            current = current.next

        current.next = None
        self.tail = current