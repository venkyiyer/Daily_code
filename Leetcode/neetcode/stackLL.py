class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
        
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return "\n".join(values)

    def isempty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self):
        if self.isempty():
            return "Stack is empty"
        else:
            poppedNode = self.LinkedList.head
            self.LinkedList.head  = poppedNode.next
            return poppedNode.value

    def peek(self):
        if self.isempty():
            return "Stack is empty"
        else:
            peekNode = self.LinkedList.head.value
            return peekNode

    def delete(self):
        self.LinkedList.head = None

customStack = Stack()
print(customStack.isempty())
customStack.push(10)
customStack.push(20)
customStack.push(30)
print(customStack)
print("****----")
customStack.pop()
print("********")
print(customStack.peek())
