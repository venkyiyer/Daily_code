class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def delete_node(self, index):
        if index < 0 or index >= self.length:
            return None
    
        elif index == 0:
            popped_node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node
    
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
    
            popped_node = temp.next
            
            # if node to be removed is the tail node
            if popped_node.next is None:
                self.tail = temp
    
            temp.next = temp.next.next
            popped_node.next = None
            self.length -= 1
            return popped_node
