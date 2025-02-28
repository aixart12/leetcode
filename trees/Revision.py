# Tree
# Traversal
# Preorder Recursive


# Inorder Recursive



# Postorder Recursive


# Preorder Iterative
def itr_preorderTraversal(root):
    if not root:
        return 
    q = deque([root])
    while q:
        curr = q.popleft()
        print(curr.value , end="")
        if curr.left :
            q.append(curr.left)
        if curr.right : 
            q.append(curr.right)


# Inorder Iterative  Left -> Root -> Right 

def itr_inorderTraversal(root):
    if not root:
        return []
    
    stack = []
    result = []
    curr = root
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        result.append(curr.val)
        
        curr = curr.right
    
    return result





# Postorder Iterative  Left ->  Right -> Root  

def postorder_traversal(root):
    if not root:
        return []
    
    stack1 = [root]  # First stack for processing nodes
    stack2 = []  # Second stack to store the postorder sequence
    result = []
    
    while stack1:
        node = stack1.pop()  # Pop from stack1
        stack2.append(node)  # Store in stack2
        
        if node.left:
            stack1.append(node.left)  # Push left child first
        if node.right:
            stack1.append(node.right)  # Push right child second
    
    while stack2:
        result.append(stack2.pop().val)  # Pop stack2 to get postorder

    return result


# Depth Recursive

def find_depth(root, target, depth=0):
    if root is None:
        return -1  # Base case: If node is None, target is not found

    if root.value == target:
        return depth  # Found the target, return current depth

    # Recursively search in left and right subtrees
    left_depth = find_depth(root.left, target, depth + 1)
    right_depth = find_depth(root.right, target, depth + 1)

    # Return the valid depth if found in either subtree
    return max(left_depth, right_depth)



# Depth Iterative

from collections import deque

def find_depth(root, k):
    if root is None:
        return -1

    queue = deque([(root, 0)])  # (node, depth) 

    while queue:
        node, depth = queue.popleft()  # O(1) operation  get the height of the particular element 

        if node.data == k:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))  # assing the height of the particulat element 
        if node.right:
            queue.append((node.right, depth + 1))

    return -1


# Height Recursive
# Helper function to find the height
# of a given node in the binary tree
def findHeightUtil(root, x):
    # Base Case
    if root is None:
        return -1, -1  # (height of subtree, height of x if found)

    # Recursively get height of left and right subtrees
    leftHeight, leftXHeight = findHeightUtil(root.left, x)
    rightHeight, rightXHeight = findHeightUtil(root.right, x)

    # Compute current node height
    currentHeight = max(leftHeight, rightHeight) + 1

    # If current node is the target node
    if root.data == x:
        return currentHeight, currentHeight

    # Return the subtree height and propagate found height if available
    return currentHeight, max(leftXHeight, rightXHeight)

def findHeight(root, x):
    _, heightOfX = findHeightUtil(root, x)
    return heightOfX



## Height Iterative

def findNode(root, x):
    if root is None:
        return None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.data == x:
            return node  # Return the target node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None  # If x is not found

# Function to compute the height of a given node
def findHeight(root, x):
    targetNode = findNode(root, x)  # Find the target node
    if targetNode is None:
        return -1  # Node not found
    
    # BFS from the target node to find max depth
    queue = deque([(targetNode, 0)])
    maxHeight = 0

    while queue:
        node, height = queue.popleft()
        maxHeight = max(maxHeight, height)
        
        if node.left:
            queue.append((node.left, height + 1))
        if node.right:
            queue.append((node.right, height + 1))

    return maxHeight  # Height of the target node




# Max depth / height Recursive
def findDepthUtil(root, x, depth):
    # Base Case: If tree is empty or node is not found
    if root is None:
        return -1

    # If current node is the target node, return its depth
    if root.data == x:
        return depth

    # Search in left and right subtrees
    leftDepth = findDepthUtil(root.left, x, depth + 1)
    rightDepth = findDepthUtil(root.right, x, depth + 1)

    # Return the depth if found in either subtree
    return max(leftDepth, rightDepth)

def findDepth(root, x):
    return findDepthUtil(root, x, 0)




# Max depth / height Iterative

from collections import deque

def find_max_height(root):
    if root is None:
        return -1  # Height of an empty tree is -1 (or 0 based on definition)

    queue = deque([(root, 0)])  # (node, depth)
    max_height = 0

    while queue:
        node, depth = queue.popleft()  # O(1) operation
        max_height = max(max_height, depth)  # Track the deepest level reached

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return max_height



# Diameter Recusrive 

def height(self, node):
        if node is None:
            return 0  # Base case: height of an empty subtree is 0
        return max(self.height(node.left), self.height(node.right)) + 1

def diameterOfBinaryTree(self, root) -> int:
    if root is None:
        return 0  # Base case: empty tree has diameter 0

    left_height = self.height(root.left)  # Compute left subtree height
    right_height = self.height(root.right)  # Compute right subtree height

    # Diameter at the current node
    diameter_at_node = left_height + right_height

    # Recursively find diameter in left and right subtrees
    left_diameter = self.diameterOfBinaryTree(root.left)
    right_diameter = self.diameterOfBinaryTree(root.right)

    # Return the maximum diameter found
    return max(diameter_at_node, left_diameter,right_diameter)

# Diameter Itterative 






