# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def traversalAcc(self, root, ret):
        if root == None:
            return ret
        
        self.traversalAcc(root.left, ret)

        ret.append(root.val)
       
        self.traversalAcc(root.right, ret)

        return ret

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.traversalAcc(root, [])

        

        