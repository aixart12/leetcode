class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def solve(root: TreeNode, res: list) -> int:
            if root is None:
                return 0

            l = solve(root.left, res)
            r = solve(root.right, res)

            temp = 1 + max(l, r)   # height to return
            ans = l + r            # possible diameter through this node
            res[0] = max(res[0], ans)

            return temp

        res = [0]
        solve(root, res)
        return res[0]
