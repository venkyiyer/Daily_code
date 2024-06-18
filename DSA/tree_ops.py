class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
new_tree = TreeNode('Drinks')
new_tree.leftChild = TreeNode('Hot')
new_tree.rightChild= TreeNode('Cold')

def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)

# preOrderTraversal(new_tree)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        inOrderTraversal(rootNode.rightChild)


# inOrderTraversal(new_tree)

def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        postOrderTraversal(rootNode.leftChild)
        postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

postOrderTraversal(new_tree)

