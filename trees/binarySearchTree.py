class TreeNode: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insertInBinaryTree(root, value: int):
    if not root:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insertInBinaryTree(root.left, value)
    else:
        root.right = insertInBinaryTree(root.right, value)
    
    return root

def searchInBST(root, value):
    if not root:
        return False  # Base case: Value not found
    
    if root.value == value:
        return True  # Value found
    
    if value < root.value:
        return searchInBST(root.left, value)  # Search in left subtree
    
    return searchInBST(root.right, value)  # Search in right subtree


#  Delete a node in tree

def findMin(root):
    """Finds the node with the smallest value in a subtree."""
    while root.left:
        root = root.left
    return root  # Leftmost node is the smallest

def deleteInBST(root , value):
    if not root : 
        return 

    if value < root.value: 
        deleteInBST(root.left , value)
    elif value > root.value:
        deleteInBST(root.right , value) 
    else:
        # Case 1: No child
        if not root.left and not root.right:
            return None  # Remove the node
        
        # Case 2 : Right Child
        if root.left is None : 
            return root.right
        
        if root.right is None:
            return root.left
        
        successor = findMin(root.right)  # Find inorder successor (smallest in right subtree)
        root.value = successor.value  # Replace node's value with successor's value
        root.right = deleteInBST(root.right, successor.value)  # Delete the successor node
    
    return root



#  Lowest Common Ancestor in BST (Leetcode 235)

def lowestCommonAncestor(root , n1 , n2):
    if not root : 
        return None
    
    if root.value > n1.value and root.value > n2.value :
        lowestCommonAncestor(root.left  , n1 , n2)
    
    if root.value < n2.value and root.value < n2.value:
        lowestCommonAncestor(root.right , n1 , n2)
    
    return root




# Check if a Binary Tree is subtree of another binary tree 
def areIdentical(root1 , root2):
    if root1 is None and root2 is None :
        return True
    if root1 is None or root2 is None : 
        return False
    return (root1.value == root2.value and areIdentical(root1.left , root2.left ) and areIdentical(root1.right , root2.right))


def isSubTree(root1 , root2):
    if not root1 :
        return False
    if not root2:
        return True
    
    if areIdentical(root1 , root2):
        return True
    
    return isSubTree(root1.left , root2) or isSubTree(root2.left , root2)



# Symmetric Tree
def isMirror(leftSub , rightSub):
    if leftSub is None and rightSub is None :
        return True
    
    if leftSub is None or rightSub is None or leftSub.value != rightSub.value :
        return False
    
    return isMirror(leftSub.left , rightSub.right) and isMirror(leftSub.right  , rightSub.left)
    
def isSymmetricTree(root):
    if not root : 
        return True
    
    return isMirror(root.left , root.right)



#  Binary Tree Right Side View (Leetcode 199)
def printRightSideView(root):
    result = []
    def dfs(node , level):
        if not node :
            return 
        
        if level == len(result):
            result.append(node.value)
        
        # Prioritize right subtree
        dfs(node.right , level + 1)
        dfs(node.left, level+1)
    
    dfs(root , 0)
    return result

# Binary Tree Left Side View 

def printLeftSideView(root):
    result = []
    
    def dfs(node, level):
        if not node:  # Fix: Use node instead of root
            return
        if level == len(result):  # First node encountered at this level
            result.append(node.value)
        
        # Prioritize the left subtree first
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    dfs(root, 0)
    return result




# Construct Binary Tree from Preorder and Inorder Traversal (Leetcode 105)
def search(inorder , value , left , right):
    for i in range(left , right+1):
        if inorder[i] == value:
            return i
    return -1


def buildTreeRecur(inorder , preorder , preIndex , left , right):
    if left > right:
        return None
    rootVal = preorder[preIndex[0]]
    preIndex[0] += 1

    root = TreeNode(rootVal)

    index = search(inorder , rootVal , left , right)

    root.left = buildTreeRecur(inorder , preorder , preIndex , left , index -1)
    root.right = buildTreeRecur(inorder, preorder , preIndex , index +1, right)

    return root

def buildTree(inorder , preorder):
    preIndex= [0]
    return buildTree(inorder , preorder , preIndex , 0 , len(preorder) -1)





# Function to print the tree (Inorder Traversal)
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.value, end=" ")
        inorderTraversal(root.right)



# Example usage:
root = None
values = [50, 30, 70, 20, 40, 60, 80]  # Values to insert

for val in values:
    root = insertInBinaryTree(root, val)

print("Inorder traversal of the tree:")
inorderTraversal(root)



# Searching for values in the BST
print(searchInBST(root, 40))  # Output: True
print(searchInBST(root, 25))  # Output: False
