from model.node import node

class base_linked_list:
    def __init__(self) -> None:
        self.element = None

    def insert_first(self, value):
        new_node = node(value)
        new_node.next = self.element
        self.element = new_node

    def insert_last(self, value):
        if not self.element:
            self.element = node(value)
            return
        
        current = self.element
        while current.next:
            current = current.next

        current.next = node(value)

    def remove_first(self):
        if not self.element:
            print('linked list is empty')
            return
        
        self.element = self.element.next

    def remove_last(self):
        if not self.element:
            print('linked list is empty')
            return
        
        if not self.element.next:
            self.element = None
            return

        current = self.element
        while current.next and current.next.next:
            current = current.next

        current.next = None