# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorder_rec(self, root, res):
        if not root:
            return
        
        self.postorder_rec(root.left, res)
        self.postorder_rec(root.right, res)
        res.append(root.val)

        

    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        self.postorder_rec(root, res)
        return res