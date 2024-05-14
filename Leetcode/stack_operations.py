class stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values  = [str(x) for x in self.list] # For LIFO
        return '\n'.join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False    
    
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
    def pop(self):
        if self.is_empty():
            return "There is no element in the stack"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.is_empty():
            return "Thers is no element in the stack"
        else:
            return self.list(len(self.list)-1)
        
    def delete(self):
        self.list = None

obj = stack()
obj.__str__()