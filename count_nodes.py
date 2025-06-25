# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        def count(root, level, ret):
            if not root:
                return

            if level >= len(ret):
                ret.append([])

            ret[level].append(root.val)

            count(root.left, level+1, ret)
            count(root.right, level+1, ret)


        ret = []
        count(root, 0, ret)

        return int(math.pow(2, len(ret)-1) + len(ret[len(ret)-1])) -1