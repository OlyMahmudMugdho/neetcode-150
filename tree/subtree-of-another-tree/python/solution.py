# Definition for a binary tree node.
from multiprocessing.util import sub_warning


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if root == subRoot == None:
            return True

        if root == None or subRoot == None:
            return False


        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        


    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p == q == None:
            return True

        if p == None or q == None:
            return False


        isSame = False

        if p.val == q.val:
            isSame = True

        return isSame and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)