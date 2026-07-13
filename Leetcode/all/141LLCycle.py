class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        new_node = ListNode(self.val)
        new_node = head

    def traverse(self, head):
        current = head
        while current:
            print(current.value)
            current = current.next

new_LL = Solution()
new_LL.hasCycle()
new_LL.traverse()
            
