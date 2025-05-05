class Solution:
    def preOrderTraversal(self, root):
        curr, stack = root, []
        res = []
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        
        return res