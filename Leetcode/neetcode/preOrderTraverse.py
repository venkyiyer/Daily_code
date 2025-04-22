class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

newBT = TreeNode('Drinks')
leftchild = TreeNode('Hot')
rightchild = TreeNode('Cold')
newBT.left = leftchild
newBT.right = rightchild


def preOrderTraversal(rootNode):
    if rootNode is None:
        return None
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)

preOrderTraversal(newBT)