class TreeNode: 
    def __init__(self , value):
        self.value = value 
        self.left  = None
        self.right = None


# Depth-First Search (DFS) Traversals

def prepreorder_traversal(node): #Root --> Left --> Right 
    if node : 
        print(node.value, end="-->")
        prepreorder_traversal(node.left)
        prepreorder_traversal(node.right)

def inorder_traversal(node):  # Left --> Root --> Right 
    if node :
        inorder_traversal(node.left)
        print(node.value, end="-->")
        inorder_traversal(node.right)

def postorder_traversal(node): 
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value , end="--> ")

# Breadth-First Search (BFS) - Level Order Traversal
from collections import deque

def level_order_traversal(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Breadth-First Search (BFS) - Level Order Traversal Without Collections Module
def level_order_traversal(root):
    if not root:
        return
    queue = [root]  # Using list as a queue
    while queue:
        node = queue.pop(0)  # Dequeue the first element
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)  # Enqueue left child
        if node.right:
            queue.append(node.right)  # Enqueue right child

def find_depth(root , target , depth=0):
    if not root:
        return -1
    if root.value == target:
        return depth
    left_depth = find_depth(root.left , target , depth + 1)
    if left_depth != -1 : 
        return left_depth
    return find_depth(root.right , target , depth + 1)


def find_height(root):
    if not root:
        return -1
    left_height = find_height(root.left)
    right_height = find_height(root.right)
    return 1 + max(left_height, right_height)


def height( node):
    if node is None:
        return 0  # Base case: height of an empty subtree is 0
    return max(height(node.left), height(node.right)) + 1

def diameterOfBinaryTree( root: TreeNode) -> int:
    if root is None:
        return 0  # Base case: empty tree has diameter 0

    left_height = height(root.left)  # Compute left subtree height
    right_height = height(root.right)  # Compute right subtree height

    # Diameter at the current node
    diameter_at_node = left_height + right_height

    # Recursively find diameter in left and right subtrees
    left_diameter = diameterOfBinaryTree(root.left)
    right_diameter = diameterOfBinaryTree(root.right)

    # Return the maximum diameter found
    return max(diameter_at_node, left_diameter,right_diameter)


# Binay tree preorder Traver using ittration # Root -> Left -> Right 
def itr_preorderTraver(root):
    if not root:
        return
    q = deque([root])
    while q : 
        node = q.popleft()
        print(node.value , end=" ")
        if node.left :
            q.append(node.left)
        if node.right : 
            q.append(node.right)

# Binary tree inorder Traverse using iitration Left -> Root -> Right 
def itr_inorderTraverse(root):
    if not root:
        return
    q = deque([root])
    while q :
        node = q.popleft()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)


# Example Tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

# # Performing Traversals
# print("Preorder Traversal:")
# prepreorder_traversal(root)  # Output: 1 2 4 5 3 6

# print("\nInorder Traversal:")
# inorder_traversal(root)   # Output: 4 2 5 1 3 6

# print("\nPostorder Traversal:")
# postorder_traversal(root) # Output: 4 5 2 6 3 1


# print("\nLevel Order Traversal:")
# print(level_order_traversal(root) )# Output: 1 2 3 4 5 6

# # Finding Depth and Height
# print("\nDepth of Node 5:", find_depth(root, 5))  # Output: 2
# print("Height of the Tree:", find_height(root))  # Output: 2

# Diameter to the tree
# print(diameterOfBinaryTree(root))

# iitr preorder 
print(itr_preorderTraver(root))


