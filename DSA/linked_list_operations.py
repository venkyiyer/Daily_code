class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

# initializing an empty linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result+= str(temp_node.value)
            if temp_node.next is not None:
                result+= '-->'
            temp_node=temp_node.next
        
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    
    def insert_at_location(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index ==0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next= temp_node.next
            temp_node.next = new_node
        self.length +=1        
        return True

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    def search_a_value(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                print('index-->', index)
            current = current.next
            index +=1
        return False    

    def get_value(self, index):
        if index == -1:
            return self.tail
        elif index <-1 or index >= self.length:
            return None
        current_node = self.head
        for _ in range(index-1):
            current_node = current_node.next
        return current_node

    def set_value(self,index, value):
        temp = self.get_value(index)
        if temp:
            temp.value = value
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
        self.length -= 1
        return popped_node
    
    def pop_last(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length ==1 :
            self.head = None
            self.tail = None
        temp = self.head
        while temp.next is not self.tail:
           temp = temp.next
        self.tail = temp
        temp.next = None
        self.length-=1
        return popped_node 

    def remove_node(self, index):
        if index >= self.length or index<-1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop_last()
        prev_node = self.get_value(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -=1
        return popped_node
    
    def remove_all(self):
        self.head = None
        self.tail = None
        self.length = 0


new_linked_list = LinkedList()
new_linked_list.append(15)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.insert_at_location(1, 25)
new_linked_list.traverse()
new_linked_list.search_a_value(30)
new_linked_list.get_value(100)
new_linked_list.set_value(1, 65)
print(new_linked_list.__str__())
         