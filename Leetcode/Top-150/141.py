class ListNode:
    def __init__(self, x):
        self.head = x
        self.next = None
    

class Solution:
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                print('True')
        print('False')