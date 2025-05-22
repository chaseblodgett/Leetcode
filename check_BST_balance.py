# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check_height(self, root):
        if not root:
            return 0

        left = self.check_height(root.left)
        if left == -1:
            return -1
        
        right = self.check_height(root.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1


        
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        if root:
                 
            return self.check_height(root) != -1
        
        return True