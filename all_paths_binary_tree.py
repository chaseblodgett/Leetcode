# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def paths_rec(self, root, res, curr_path):

        if not root:
            return

        curr_path += str(root.val)
        if not root.left and not root.right:
            res.append(curr_path)

        curr_path += "->"
        
        self.paths_rec(root.left, res, curr_path)
        self.paths_rec(root.right, res, curr_path)

        

    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if root:
            res = []
            curr_path = ""
            self.paths_rec(root, res, curr_path)
            return res
        return []