# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        preorder = []
        def pre_order(node):
            if not node:
                return

            preorder.append(node)
            pre_order(node.left)
            pre_order(node.right)
        
        pre_order(root)

        for i in range(len(preorder)-1):
            preorder[i].left = None
            preorder[i].right = preorder[i+1]

        return root