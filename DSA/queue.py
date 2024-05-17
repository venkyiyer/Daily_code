# FIFO 
class queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)
        return 'Item is inserted at the end of the queue'
    
    def deque(self):
        if self.isEmpty:
            return 'No element to deque'
        else:
            return self.items.pop(0) # removing the first element from the queue
    
    def peek(self):
        if self.isEmpty:
            return 'List is empty'
        else:
            return self.items[0]
    
    def delete(self):
        self.items = None
        