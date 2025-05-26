# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def left_sum_rec(self, root, left_leaves, is_left):
        if not root:
            return
        
        self.left_sum_rec(root.left, left_leaves, True)
        self.left_sum_rec(root.right, left_leaves, False)
        
        if is_left and not root.left and not root.right:
            left_leaves.append(root)
            
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        left_leaves = []
        self.left_sum_rec(root, left_leaves, False)
        total_sum = 0
        for leaf in left_leaves:
            total_sum += leaf.val
        return total_sum