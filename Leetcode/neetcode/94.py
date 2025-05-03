class Solution:
    def inOrderTraversal(self, root):
        res = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            res.append(current)
            current = current.right
