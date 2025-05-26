class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def solve(root: TreeNode, res: list) -> int:
            if root is None:
                return 0
            
            l = solve(root.left, res)
            r = solve(root.right, res)

            temp = max(max(l, r) + root.val, root.val)
            ans = max(temp, l + r + root.val)
            res[0] = max(res[0], ans)

            return temp
        res = [float('-inf')]
        solve(root, res)
        return res[0]

# Example tree:
#      10
#     /  \
#    2   10
#   / \    \
#  20  1    -25
#           / \
#          3   4

root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(10)
root.left.left = TreeNode(20)
root.left.right = TreeNode(1)
root.right.right = TreeNode(-25)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)

sol = Solution()
print(sol.maxPathSum(root))  # Output should be 42
