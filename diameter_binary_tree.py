# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_diameter = 0
        def dfs(node):
            if not node:
                return 0
            
            elif node.left and not node.right:
                return dfs(node.left) + 1
            
            elif node.right and not node.left:
                return dfs(node.right) + 1
            
            return max(dfs(node.right), dfs(node.left)) + 1
        
        max_diameter = 0
        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                max_diameter = max(dfs(node.left) + dfs(node.right), max_diameter)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return max_diameter