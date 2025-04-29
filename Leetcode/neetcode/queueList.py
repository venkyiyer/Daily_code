class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def is_empty(self):
        if self.items == []:
            return True
        return False

    def enqueue(self, value):
        self.items.append(value)
        return 'element inserted!'

    def dequeue(self):
        if self.is_empty():
            return 'The queue is empty!'
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return 'The queue is empty'
        return self.items[0]

    def delete(self):
        self.items = None
        
customQueue = Queue()
print(customQueue.is_empty())
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
print(customQueue)