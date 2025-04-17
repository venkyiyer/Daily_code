class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
        
        if lis == lis[::-1]:
            return True
        return False