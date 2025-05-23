# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        if p and not q:
            return False
        elif q and not p: 
            return False
        elif not q and not p:
            return True
        elif q.val != p.val:
            return False   

        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right, q.right)
        
        return left and right