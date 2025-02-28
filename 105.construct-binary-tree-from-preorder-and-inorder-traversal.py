#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIndex = [0]
        return self.buildTreeRecur(preorder , inorder , preIndex , 0 , len(preorder) -1)

        
    def buildTreeRecur(self , preorder , inorder , preIndex , left , right ):
        # base case
        if left > right:
            return None

        rootValue = preorder[preIndex[0]]
        preIndex[0] += 1
        rootIndex = self.search(inorder ,rootValue, left , right)

        root = TreeNode(rootValue)

        root.left = self.buildTreeRecur(preorder , inorder, preIndex , left , rootIndex -1 )
        root.right = self.buildTreeRecur(preorder , inorder ,preIndex , rootIndex+1 , right )

        return root

    def search(self ,inorder , rootValue , left , right):
        for i in range(left , right+1):
            if inorder[i] == rootValue:
                return i
        return -1

# @lc code=end

