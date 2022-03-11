class Node:

    def __init__(self, value = None):
        self.value = value
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insertSingleLinkedList(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node 
            else:
                tempnode = self.head
                index = 0
                while index < location -1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = new_node
                new_node.next = nextnode
                if tempnode == self.tail:
                    self.tail = new_node

    def traverseSingleLinkedList(self):
        if self.head is None:
            print('Linked list does not exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next 
    
    def searchSinglyLinkedList(self, searchvalue):
        if self.head is None:
            print('Linked list does not exist')
        else:
            node = self.head
            while node is not None:
                if node.value == searchvalue:
                    return node.value
                node.next
                return 'The value does not exist'
