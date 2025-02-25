class Node:
    def __init__(self , key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# A utility function to get the 
#  height of the tree

def  height(node):
    if not node:
        return 0
    return node.height

# A utitly fucnction to right rotate
#  subtree rotated with y

def right_rotate(y):
    x = y.left
    T2 = x.right

    # Perform roatiotion 
    x.right = y
    y.left = T2

    # Update heights
    y.height = 1 + max(height(y.left) , height(y.right))
    x.height = 1 + max(height(x.left) , height(x.right))
    
    return x

def left_rotation(x):
    y = x.right
    T2 = y.left

    # Perform rotation 
    y.left = x
    x.right = T2

    # Update heights
    x.height = 1 + max(height(x.left) , height(x.right))
    y.height = 1 + max(height(y.left) , height(y.right))

    return y

# Get balance factor of node N
def get_balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)


# Recusive function to insert a key in 
# the subtree rooted with node

def insert(node , key):
    
    # Perfomr the normal BST insertion 
    if not node : 
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left ,key )
    elif key > node.key:
        node.right = insert(node.right , key)
    else: 
        # equal keys are node allowed in BST
        return node
    
    # Update height of this ancestor node
    node.height = 1 + max(height(node.left) , height(node.right))

    # Get the balance factor of this ancestor node 
    balance = get_balance(node)

    # If the node becomes unbalanced, 
    #  then ther are 4 cases

    #  Left left case
    if balance > 1 and key < node.left.key:
        return right_rotate(node)
    
    # Right Right Case
    if balance < -1 and key > node.right.key:
        return left_rotation(node)
    
    # Left Right Case
    if balance > 1 and key > node.left.key:
        node.left = left_rotation(node.left)
        return right_rotate(node)
    
    # Right Left Case
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotation(node)
    
    # Return the (unchanged) node pointer

    return node

def min_value_node(node):
    current = node

    # Loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current


def delete_node(root , key):
    # STEP 1 : perform standard bst delete
    if root is None:
        return root
    
    # If the key to be deleted is greater 
    # than the root's key , then it lies in right subtree
    elif key > root.key:
        root.right = delete_node(root.right , key)

    # if key is same as root's key , then 
    else:
        #node with only one child or no child
        if root.left is None or root.right is None:
            temp = root.left if root.left else root.right

            # No child case
            if temp is None:
                root = None
            else:
                root = temp

        else:
            # node witho tow children : Get the 
            # inorder sucessor ( smallest in 
            # the right subtee )
            temp = min_value_node(root.right)

            # Copy the inorder sucessor's
            # data to this node
            root.key = temp.key 

            # Delete the inorder sucessor 
            root.right = delete_node(root.right , temp.key)

    if root is None:
        return root
    
    # STEP 2 : update height of the current node
    root.height = max(height(root.height), height(root.right)) + 1

    # STEP 3 : get the balance factor or this node ( to check whether this 
    # node became unbalanced )

    balance= get_balance(root)

    # If this node becomes unbalanced , then there are 4 cases

    # Left left Case
    if balance > 1 and get_balance(root.left) >=0:
        return right_rotate(root)
    
    # Left Right Case
    if balance > 1 and get_balance(root.left) < 0: 
        root.left = left_rotation(root.left)
        return right_rotate(root)
    
    # Right Right case
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotation(root)
    
    # Right left Case
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotation(root)
    
    return root





def pre_order(root):
    if root:
        print(root.key , end=" ")
        pre_order(root.left)
        pre_order(root.right)
        
# Driver code
root = None

#  Constructiong tree given in the above figure
root = insert(root , 10)
root = insert(root , 20)
root = insert(root , 30)
root = insert(root , 40)
root = insert(root , 50)
root = insert(root , 25)



# The constructed AVL Tree would be
#        30
#       /  \
#      20   40
#     /  \    \
#    10  25   50

print("Preorder traversal : ")
pre_order(root)
root = delete_node(root, 10)

print("\nPreorder traversal after"
        " deletion of 10")
pre_order(root)

    



