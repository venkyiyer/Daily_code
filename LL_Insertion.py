



class Node:

    def __init__(self, value= None):
        self.value = value
        self.next = None 
        

class SinglyLL:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location ==0:
                new_node.next = self.head
                self.head = new_node 
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node # previous last node's reference
                self.tail = new_node
            else:
                tempnode = self.head # traverse from the start
                index = 0
                while index < location -1: # location marks the location where new node has to be inserted! So, traverse till that point 
                    tempnode = tempnode.next # A tempnode to store the references - Gives the current nodes reference
                    index +=1 # incrementing the index
                nextnode = tempnode.next # Givet the refetence of the next node. - We have to insert a node between current node and the it's next node.
                tempnode.next  = new_node # current elment is tempnode, so pointing it to the new node
                new_node.next = nextnode # Pointing the new node to the next node


