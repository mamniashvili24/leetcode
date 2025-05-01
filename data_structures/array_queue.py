class array_queue:
    def __init__(self) -> None:
        self.my_stack = []

    def enqueue(self, element):
        self.my_stack.append(element)

    def dequeue(self):
        self.my_stack.pop(0)

    def peek(self):
        return self.my_stack[0]
    
    def is_empty(self):
        return len(self.my_stack) == 0
    
    def __len__(self):
        return len(self.my_stack)