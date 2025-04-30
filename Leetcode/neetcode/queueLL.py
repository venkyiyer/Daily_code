class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        currNode = self.head 
        while currNode:
            yield currNode
            currNode = currNode.next

class Queue:
    def __init__(self):
        self.ll = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.ll]
        return ' '.join(values)

    def enque(self, value):
        newNode = Node(value)
        if self.ll.head == None:
            self.ll.head = newNode
            self.ll.tail = newNode
        else:
            self.ll.tail.next = newNode
            self.ll.tail = newNode
    
    def isempty(self):
        if self.ll.head == None:
            return 'Queue is empty'
        return False
    
    def dequeue(self):
        if self.isempty():
            return 'Queue is empty'
        else:
            tempNode = self.ll.head
            if self.ll.head == self.ll.tail:
                self.ll.head = None
                self.ll.tail = None
            else:
                self.ll.head = self.ll.head.next
            
            return tempNode
    
    def peek(self):
        if self.isempty():
            return 'Queue is empty'
        else:
            return self.ll.head
    
    def delete(self):
        self.ll.head = None
        self.ll.tail = None

customQueue = Queue()
customQueue.enque(10)
customQueue.enque(20)
customQueue.enque(30)
print(customQueue)