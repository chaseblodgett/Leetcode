# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def check_depth_rec(node):
            if not node.left and not node.right:
                return 1
            
            elif node.left and not node.right:
                return check_depth_rec(node.left) + 1
            
            elif node.right and not node.left:
                return check_depth_rec(node.right) + 1
            
            return min(check_depth_rec(node.right), check_depth_rec(node.left)) + 1

        if root:
            return check_depth_rec(root)
        else:
            return 0