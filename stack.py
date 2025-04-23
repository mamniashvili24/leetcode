class stack:
    def __init__(self) -> None:
        self.my_list = []

    def push(self, element):
        self.my_list.append(element)

    def pop(self):
        self.my_list.pop()

    def peek(self):
        return self.my_list[-1]
    
    def is_empty(self):
        return len(self.my_list) == 0
    
    def __len__(self):
        return len(self.my_list)