# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def rec(root, ret):
            if root == None:
                return

            rec(root.left, ret)

            ret.append(root.val)

            rec(root.right, ret)

        ret = []

        rec(root, ret)

        for i in range(1, len(ret)):
            if ret[i-1] >= ret[i]:
                return False

        return True 