# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0

        current = root
        right = 0
        while current.right:
            right += 1
            current = current.right

        current = root
        left = 0

        while(current.left):
            left += 1
            current = current.left

        return left + right