from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Inside your Solution class
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack, prev_val, min_diff = [], None, float('inf')

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if prev_val is not None:
                min_diff = min(min_diff, root.val - prev_val)

            prev_val = root.val
            root = root.right

        # If min_diff is still float('inf'), it means there was no meaningful difference found
        return min_diff if min_diff != float('inf') else 0
