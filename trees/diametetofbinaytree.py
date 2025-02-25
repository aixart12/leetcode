class TreeNode:
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, node):
        if node is None:
            return 0  # Base case: height of an empty subtree is 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
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