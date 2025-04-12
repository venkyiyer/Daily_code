class Solution:
    def middleNode(self, head, length):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
