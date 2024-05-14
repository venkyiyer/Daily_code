class stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list)== self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return 'Stack is full'
        else:
            self.list.append(value)
            return 'value is successfully inserted'
    
    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'
        else:
            self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return 'Stack is empty'
        else:
            return len((self.list)-1)
        
    def delete(self):
        self.list = None
        return 'Deleted the stack!'

cstack = stack(4)
print(cstack.isEmpty())
print(cstack.isFull())
cstack.push(1)
cstack.push(2)
cstack.push(3)
print(cstack.isFull())
print(cstack)

    

