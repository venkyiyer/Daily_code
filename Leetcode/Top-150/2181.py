class Node:
    def __init__(self, value= 0, next = None):
        self.value = value
        self.next = next

class LL:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

class Solution:
    def mergeNodes(self, head):
        curr = head
        tail = dummy = Node()

        while curr.next:
            node = Node(0)
            while curr.next.val!= 0:
                node.val += curr.next.val
                curr = curr.next
            tail.next = node
            tail = tail.next
            curr = curr.next
        
        return dummy.next

