class Node:
    def __init__(self, value = None):
        #  Currently keeing the node value as none. While creating the node, pass the node value : self.value = value. ## E.g newnode = Node(2)
        self.value = value
        # And reference of the node as NULL
        self. next = None


class singlyLinkedList:
    
    def __init__(self):
        # Assigning null reference to the head
        self.head = None
        # Assigning null reference to the tail 
        self.tail = None

    '''# Creating an object for the class singlyLinkedList
    singlyLL = singlyLinkedList()   
    # Creating a new node with the value as 1,2,3
    newNode1 = Node(1)
    newNode2 = Node(2)
    newNode3 = Node(3)
    # This means : The head vlaue of the LL is Node(1)
    singlyLL.head = newNode1
    # This means: singly.head  = newnode; so, the reference (next) of the newnode1 is pointing to the physical location of the next node i.e node2 
    singlyLL.head.next = newNode2
    # As an example - Check the below line . How we can point to the physical location of node3.
    singlyLL.head.next.next = newNode3
    '''
    def insertnode(self, value, location):
        # creating a new node
        newnode = Node(value)
        # When head is none - This means - The linked list is empty 
        if self.head is None:
            # Then point the refernce of the head to newnode (physical location of the newnode)
            self.head  = newnode
            # Then point the reference of the tail to new node (Because it is the only node in the LL - Physical location of the new node)
            self.tail = newnode
        else: 
            # If we want to insert at location 0. i.e beginging of the LL
            if location == 0:
                # Whatever reference was in the head -- assign it to the newnode (Because newnode is the new element and it should point to the previous first element)
                newnode.next = self.head
                # And now, assign the head to the newnode
                self.head = newnode
            elif location == -1:
                # As newnode is the last node, point it's reference to Null
                newnode.next = None
                # Assing the last node's reference to the newnode (previous last to the newnode -- as newnode is the last node now)
                self.tail.next = newnode
                # assign the tails to the newnode --as new node has become the last element
                self.tail = newnode
            else:
                # To traverse, we start from the first node -- which the head is pointing to
                tempnode = self.head
                # maintain a counter 
                index = 0
                while index < location -1:
                    # Current node (current node) will always point to the next node in the LL. -- You will know the poition to insert the newnode
                    currentnode = currentnode.next
                    # increase the counter
                    index += 1
                # newnode will point to the next node. 
                newnode = currentnode.next
                # current nodes reference pointed to the new node
                currentnode.next = newnode
                # newnodes pointer to the newnode -- currentnode.next
                newnode.next = newnode

    def traversalLL(self):
        if self.head is None:
            print('Single LL does not exist')
        else:
            currentnode = self.head
            while currentnode is not None:
                print(currentnode.value)
                currentnode = currentnode.next 

    def searchElementLL(self, element):
        if self.head is None:
            print('LL does not exist')
        else:
            currentnode = self.head
            while currentnode is not None:
                if currentnode.value == element:
                    print('Found the element', currentnode.value)
                else:
                    print('value not found')


    def deleteNode(self, location):
        if self.head is None:
            print('The LL is empty')
        else:
            if location ==0:
                if self.head == self.tail:
                    self.head = None 
                    self.tail = None
                else:
                    self.head  =self.head.next
            if location == 1:
                if self.head == self.tail:
                    self.head = None 
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break


        













        