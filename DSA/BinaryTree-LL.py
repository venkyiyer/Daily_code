class treeNode:

    def __init__(self, data):
        self.data = data # value of the node
        self.leftchild = None # Reference for the left child # Both the childs will be empty because only the root exists as of now and the tree is empty!
        self.rightchild = None # Reference to the right child

newBT = treeNode('Drinks') # Creating a tree with the root node value as 'Drinks'
leftchild = treeNode('Hot') # creating left child of the root node
leftchild.leftchild = treeNode('Tea')
leftchild.rightchild = treeNode('Coffee')
rightchild = treeNode('Cold') # creating right child of the root node
rightchild.leftchild = treeNode('Fanta')
rightchild.rightchild = treeNode('Coke')
newBT.leftchild = leftchild # linking it to the root
newBT.rightchild = rightchild # linking it to the root 

def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    print(preOrder(rootNode.leftchild))
    print(preOrder(rootNode.rightchild))

def inOrder(rootNode):
    if not rootNode:
        return
    print(inOrder(rootNode.leftchild))
    print(rootNode.data)
    print(inOrder(rootNode.rightchild))

def postOrder(rootNode):
    if not rootNode:
        return
    print(postOrder(rootNode.leftchild))
    print(postOrder(rootNode.rightchild))
    print(rootNode.data)

def searchElement(rootNode, nodeValue):
    if not rootNode:
        return 'Binary tree does not exist'
    else:
        preOrder(rootNode.leftchild) == nodeValue
    elif preOrder(rootNode.rightchild)


    