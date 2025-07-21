'''Inserting,Preorder,postorder,inorder
height of tree
Insertion into BST
Sum of all nodes
Sum of even nodes
Search in Bst
DFS Traversal
Count of Leaf nodes
All paths form root to leaves
Views OF TREE
LEAST COMMON ANCESTOR(LCA)
IS TREE BALANCED OR NOT???
'''
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Insert node
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Traversals
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

# Sum
def sum_nodes(root):
    if root is None:
        return 0
    return root.data + sum_nodes(root.left) + sum_nodes(root.right)

def sum_even_nodes(root):
    if root is None:
        return 0
    s = root.data if root.data % 2 == 0 else 0
    return s + sum_even_nodes(root.left) + sum_even_nodes(root.right)

# Height
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

# Search
def search_bst(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search_bst(root.left, key)
    else:
        return search_bst(root.right, key)

# DFS
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

# Leaf count
def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

# All root-to-leaf paths
def print_all_paths(root, path=None):
    if path is None:
        path = []
    if root is None:
        return
    path.append(root.data)
    if root.left is None and root.right is None:
        print(" -> ".join(map(str, path)))
    else:
        print_all_paths(root.left, path[:])
        print_all_paths(root.right, path[:])

# Level order traversal
def level_order_traversal(root):
    if root is None:
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.data, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
            
def is_balanced(root):
    def check_balance(node):
        if node is None:
            return 0, True
        
        left_height, is_left_bal = check_balance(node.left)
        right_height, is_right_bal = check_balance(node.right)

        current_balanced = abs(left_height - right_height) <= 1

        return 1 + max(left_height, right_height), is_left_bal and is_right_bal and current_balanced

    height, balanced = check_balance(root)
    return balanced


# Left View
def left_view(root, c):
    if root is None:
        return
    if c not in left_view_dict:
        left_view_dict[c] = root.data
    left_view(root.left, c + 1)
    left_view(root.right, c + 1)

# Right View
def right_view(root, c):
    if root is None:
        return
    if c not in right_view_dict:
        right_view_dict[c] = root.data
    right_view(root.right, c + 1)
    right_view(root.left, c + 1)

# Top View using vertical distance
def top_view(root, c, l):
    if root is None:
        return
    if c not in top_view_dict or l < top_view_dict[c][1]:
        top_view_dict[c] = (root.data, l)
    top_view(root.left, c - 1, l + 1)
    top_view(root.right, c + 1, l + 1)

# Bottom View using vertical distance
def bottom_view(root, c, l):
    if root is None:
        return
    if c not in bottom_view_dict or l >= bottom_view_dict[c][1]:
        bottom_view_dict[c] = (root.data, l)
    bottom_view(root.left, c - 1, l + 1)
    bottom_view(root.right, c + 1, l + 1)


'''
Given a BST,when two nodes are given ,we need to give the lowest common ancestor
LCA(LOWEST COMMON ANCESTOR)'''
# Lowest Common Ancestor in BST
def lowest_common_ancestor(root, p, q):
    if root is None:
        return None
    # If both nodes are smaller than root, LCA lies in left
    if p < root.data and q < root.data:
        return lowest_common_ancestor(root.left,p,q)
    # If both nodes are greater than root, LCA lies in right
    if p> root.data and q> root.data:
        return lowest_common_ancestor(root.right,p,q)
    # Else, this node is the LCA
    return root

'''CHECK IF ALL THE NODES IN A TREE IS BALANCED OR NOT
IS GIVEN TREE BALANCED OR NOT???'''

# Build tree
values = [50, 30, 20, 40, 70, 60, 80]
root = None
for val in values:
    root = insert(root, val)

# Outputs
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
print("Level Order Traversal:")
level_order_traversal(root)

# Views with global dicts
left_view_dict = {}
right_view_dict = {}
top_view_dict = {}
bottom_view_dict = {}

left_view(root, 0)
right_view(root, 0)
top_view(root, 0, 0)
bottom_view(root, 0, 0)

print("\nLeft View of Tree:")
for k in sorted(left_view_dict):
    print(left_view_dict[k], end=' ')

print("\nRight View of Tree:")
for k in sorted(right_view_dict):
    print(right_view_dict[k], end=' ')

print("\nTop View of Tree:")
for k in sorted(top_view_dict):
    print(top_view_dict[k][0], end=' ')

print("\nBottom View of Tree:")
for k in sorted(bottom_view_dict):
    print(bottom_view_dict[k][0], end=' ')
    print("-----------------------------------------------------")
    
print("Is the Tree Balanced?:", is_balanced(root))

    
# Find and print LCA
n1, n2 = 20, 40  # You can change these values to test others
lca_node = lowest_common_ancestor(root, n1, n2)
if lca_node:
    print(f"\nLowest Common Ancestor of {n1} and {n2} is: {lca_node.data}")
else:
    print(f"\nLowest Common Ancestor of {n1} and {n2} not found.")


    
