# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        def levelOrder(root, ret, level):
            if not root:
                return
            
            if len(ret) <= level:
                ret.append([])

            if level % 2 == 0:
                ret[level].append(root.val)
            else:
                ret[level].insert(0, root.val)

            levelOrder(root.left, ret, level+1)
            levelOrder(root.right, ret, level+1)
            

        ret = []
        levelOrder(root, ret, 0)
        return ret