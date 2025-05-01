class array_stack:
    def __init__(self) -> None:
        self.my_stack = []

    def push(self, element):
        self.my_stack.append(element)

    def pop(self):
        self.my_stack.pop()

    def peek(self):
        return self.my_stack[-1]
    
    def is_empty(self):
        return len(self.my_stack) == 0
    
    def __len__(self):
        return len(self.my_stack)