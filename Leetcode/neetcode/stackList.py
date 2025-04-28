class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return self.list

    def pop(self):
        if self.list == []:
            return 'No element in the stack'
        else:
            return self.list.pop()
    
    def peek(self):
        if self.list == []:
            return 'No element in the stack'
        else:
            return self.list[len(self.list)-1]
    
    def delete(self):
        self.list = None

getStack = Stack()
getStack.push(15)
getStack.push(16)
getStack.pop()
print(getStack)