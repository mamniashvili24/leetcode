from linked_list import linked_list

class linked_list_queue:
    def __init__(self) -> None:
        self.my_stack = linked_list()

    def enqueue(self, element):
        self.my_stack.insert_last(element)

    def dequeue(self):
        self.my_stack.remove_first()

    def peek(self):
        return self.my_stack.get_first()
    
    def is_empty(self):
        return len(self.my_stack) == 0
    
    def __len__(self):
        return len(self.my_stack)