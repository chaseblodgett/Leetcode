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
        
        def rec(root, ret):
            if not root:
                return
            
            ret.append(root)

            rec(root.left, ret)
            rec(root.right, ret)


            root.right = None
        
        ret = []
        rec(root, ret)

        for i in range(len(ret) -1):
            ret[i].left = None
            ret[i].right = ret[i+1]
        
        return root