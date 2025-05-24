# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invert_rec(self, root):
        if not root: 
            return 

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invert_rec(root.left)
        self.invert_rec(root.right)

    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.invert_rec(root)
        return root