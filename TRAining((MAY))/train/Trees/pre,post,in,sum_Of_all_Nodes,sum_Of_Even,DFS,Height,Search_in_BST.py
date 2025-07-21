'''Inserting,Preorder,postorder,inorder
height of tree
Insertion into BST
Sum of all nodes
Sum of even nodes
Search in Bst
DFS Traversal
Count of Leaf nodes
All paths form root to leaves
'''

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Insert node into BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

# Preorder Traversal
def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

# Postorder Traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

# Sum of all nodes
def sum_nodes(root):
    if root is None:
        return 0
    return root.data + sum_nodes(root.left) + sum_nodes(root.right)

# Sum of even nodes
def sum_even_nodes(root):
    if root is None:
        return 0
    s = 0
    if root.data % 2 == 0:
        s += root.data
    s += sum_even_nodes(root.left) + sum_even_nodes(root.right)
    return s

# Height of the tree
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

# Search in BST
def search_bst(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search_bst(root.left, key)
    else:
        return search_bst(root.right, key)

# DFS traversal (preorder)
def dfs(root):
    if root is None:
        return
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.data, end=' ')
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

# Count leaf nodes
def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left == None and root.right == None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


def print_all_paths(root, path=None):
    if path is None:
        path = []

    if root is None:
        return

    # Append current node to the path
    path.append(root.data)

    # If it's a leaf node, print the path
    if root.left is None and root.right is None:
        print(" -> ".join(map(str, path)))
    else:
        # Recursive calls for left and right subtrees
        print_all_paths(root.left, path[:])  # pass a copy of path
        print_all_paths(root.right, path[:])

    
values = [50, 30, 20, 40, 70, 60, 80]
root = None
for val in values:
    root = insert(root, val)

print("Inorder Traversal:")
inorder(root)
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)

print("\n\nSum of all nodes:", sum_nodes(root))
print("Sum of even nodes:", sum_even_nodes(root))
print("Height of tree:", height(root))
print("Search 60 in BST:", search_bst(root, 60))
print("DFS Traversal:")
dfs(root)
print("\nCount of Leaf Nodes:", count_leaf_nodes(root))
print("All Root-to-Leaf Paths:")
print_all_paths(root)