# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root == None:
            return True

        lefth = self.getLeftHeight(root.left)
        righth = self.getRightHeight(root.right)

        return abs(lefth-righth) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)


    def getLeftHeight(self, root: TreeNode | None) -> int:
        if root == None:
            return 0

        return 1 + max(
            self.getLeftHeight(root.left),
            self.getLeftHeight(root.right)
        )

    def getRightHeight(self, root: TreeNode | None) -> int:
        if root == None:
            return 0
        
        return 1 + max(
            self.getRightHeight(root.left),
            self.getRightHeight(root.right)
        )