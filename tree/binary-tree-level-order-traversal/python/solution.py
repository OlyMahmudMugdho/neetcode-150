# Definition for a binary tree node.
from collections import deque
from unittest import result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root == None:
            return []

        result = []

        queue = deque()

        queue.append(root)

        while(queue):
            level = queue

            level_values = []

            for i in range(len(level)):
                node = level.popleft()
                level_values.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            result.append(level_values)

        return result