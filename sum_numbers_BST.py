# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def rec(root, curr, ret):
            if not root: 
                return
            
            if not root.left and not root.right:
                ret.append(curr + str(root.val))
            
            rec(root.left, curr + str(root.val), ret)
            rec(root.right, curr + str(root.val), ret)

        ret = []
        rec(root, "", ret)

        total = 0
        for num in ret:
            total += int(num)
        
        return total