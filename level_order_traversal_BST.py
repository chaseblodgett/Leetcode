# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        def rec(root, level, ret):
            if not root:
                return
            
            if level >= len(ret):
                ret.append([])
            ret[level].append(root.val)

            rec(root.left, level+1, ret)
            rec(root.right, level+1, ret)

        
        ret = []
        rec(root, 0, ret)
        return ret