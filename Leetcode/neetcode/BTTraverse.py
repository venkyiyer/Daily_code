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

def inOrderTraversal(rootNode):
    if not rootNode:
        return None
    inOrderTraversal(rootNode.left)
    print(rootNode.data)
    inOrderTraversal(rootNode.right)

def postOrderTraversal(rootNode):
    if not rootNode:
        return None

    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data)

preOrderTraversal(newBT)
inOrderTraversal(newBT)
postOrderTraversal(newBT)