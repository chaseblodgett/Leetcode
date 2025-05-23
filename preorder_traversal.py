# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorder_rec(self, root, res):
        if not root: 
            return
        
        res.append(root.val)
        self.preorder_rec(root.left, res)
        self.preorder_rec(root.right, res)

        return

    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        self.preorder_rec(root, res)
        return res