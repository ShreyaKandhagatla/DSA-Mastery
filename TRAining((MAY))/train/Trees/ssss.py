class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def addNode(self, newData):
        pass

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=' ')
        self.inorder(node.right)
    

    def preorder(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=' ')

    def dfs(element):
        pass

    def bfs(element):
        pass

    def display():
        pass

def findSum(node, s):
    if node is None:
        return 0
    s = s + node.data + findSum(node.left, s) + findSum(node.right, s)
    return s

tree1 = Tree
tree1.root = Node(10)
tree1.root.left = Node(5)
tree1.root.right = Node(20)
tree1.root.left.left = Node(2)
tree1.root.right.right = Node(8)
tree1.root.left.left = Node(15)
tree1.root.right.right = Node(22)
tree1.display()

print(findSum(tree1.root, 0))
print(inorder())