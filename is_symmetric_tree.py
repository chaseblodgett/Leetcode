# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def level_order_rec(self, node, level, res):
        if node is None:
            
            if len(res) <= level:
                res.append([])
            res[level].append(None)
            return
        
        if len(res) <= level:
            res.append([])
        
        res[level].append(node.val)

        self.level_order_rec(node.left, level + 1, res)
        self.level_order_rec(node.right, level + 1, res)
        
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        res = []
        if root:    
            self.level_order_rec(root, 0, res)

            for level in res:
                for i in range(len(level) // 2):
                    if level.pop() != level[i]:
                        return False
            
            return True
        else:
            return True

    