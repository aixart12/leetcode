class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None



# Ittrative function for inorder  tree treversal 
def inOrder(root):
    ans = []
    stack = []
    curr = root

    while curr is not None or len(stack) > 0:

        # Reach the left most Node of the curr Node
        while curr is not None:

            # Place the pointer to a tree node on 
            #  the stack before traversing
            # the node's left subtree
            stack.append(curr)
            curr = curr.left
        # Current must be None at this point 

        curr = stack.pop()
        ans.append(curr.data)

        #  we have visited the node and its left subtree,
        #  Now , it's right subtree's turn 
        curr = curr.right

    return ans

# TODO : complete the post order iterative 
# def postOrderIterative(root):
#     # check the empty tree
#     if root is None:
#         return 
    
#     ans = []
#     stack = []

#     while(True):
#         while(root):



def printList(v):
    print(" ".join(map(str, v)))
  
# Constructed binary tree is
#          1
#        /   \
#      2      3
#    /  \
#  4     5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

res = inOrder(root)
printList(res)

