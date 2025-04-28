class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def isempty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

customStack = Stack()
print(customStack.isempty())