# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:

        if root == None:
            return []

        queue = deque()
        queue.append(root)

        result = []

        while(queue):
            level = queue

            result.append(level[-1].val)

            for _ in range(len(level)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return result
