# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, root:TreeNode, mx: int):
        if root == None:
            return 0

        good = 0
        if root.val >= mx:
            good = 1

        mx = max(root.val, mx)
        
        return good + self.dfs(root.left, mx) + self.dfs(root.right, mx)