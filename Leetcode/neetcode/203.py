class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        dummyNode = ListNode(next= head)
        prev, current = dummyNode, head
        while current:
            nxt = current.next
            if current.val == val:
                prev.next = nxt
            else:
                prev = current
            
            current = current.next
        
        return dummyNode.next