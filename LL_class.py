class Node:

    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    
    def __init__(self, values = None):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next