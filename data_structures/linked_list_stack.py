from linked_list import linked_list

class linked_list_stack:
    def __init__(self) -> None:
        self.my_stack = linked_list()

    def push(self, element):
        self.my_stack.insert_last(element)

    def pop(self):
        self.my_stack.remove_last()

    def peek(self):
        return self.my_stack.get_last()
    
    def is_empty(self):
        return self.my_stack.count == 0
    
    def __len__(self):
        return self.my_stack.count