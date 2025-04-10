class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length =0

    def __str__(self):
        tempNode = self.head
        result = ''
        while tempNode is not None:
            result += str(tempNode.value)
            if tempNode.next is not None:
                result += '->'
            tempNode = tempNode.next
        
        return result

    def append(self, value):
        new_node  = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length +=1
    
    def insert(self, value, index):
        new_node = Node(value)
        if index <0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1
        return True

    def traverse(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next

    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index +=1
        return -1

    def get(self, index):
        if index<-1 or index > self.length:
            return None
        if index == -1:
            return self.tail.value
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            
            return current
    
    def set(self, index, target):
        # current = self.head
        # for _ in range(index):
        #     current = current.next
        # current.value = target
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = target 
            return True
        return False

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -=1
        
        return popped_node

    def pop_last(self):
        popped_node = self.tail
        temp = self.head
        while temp.next is not self.tail:
            temp = temp.next
        self.tail = temp
        temp.next = None
        self.length -=1


new_linked_list = LinkedList()  
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.prepend(14)
new_linked_list.insert(33,1)
print(new_linked_list)
new_linked_list.traverse()
print("SEARCH-->", new_linked_list.search(24))
print("GET-->", new_linked_list.get(-1))
new_linked_list.set(2, 35)
print(new_linked_list)