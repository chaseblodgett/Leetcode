# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def check_sum(node, target):
          
            if not node.left and not node.right and target - node.val == 0:
                return True
            
            elif not node.left and not node.right and target - node.val != 0:
                return False
            
            left, right = False, False

            if node.left:
                left = check_sum(node.left, target- node.val)
            
            if node.right:
                right = check_sum(node.right, target - node.val)

            return left or right
        
        if root:
            return check_sum(root, targetSum)
        
        return False