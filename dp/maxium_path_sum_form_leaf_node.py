class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLeafToLeafPathSum(self, root: TreeNode) -> int:
        def solve(root: TreeNode, res: list) -> int:
            if root is None:
                return 0

            # Leaf node
            if not root.left and not root.right:
                return root.val

            l = solve(root.left, res)
            r = solve(root.right, res)

            # If both children exist, check leaf-to-leaf path
            if root.left and root.right:
                temp = max(l, r) + root.val
                ans = l + r + root.val
                res[0] = max(res[0], ans)
                return temp

            # If only one child exists, return path through that child
            return (l + root.val) if root.left else (r + root.val)

        res = [float('-inf')]
        total = solve(root, res)

        # If res[0] wasn't updated (e.g., only one leaf exists), return total path sum
        return res[0] if res[0] != float('-inf') else total
