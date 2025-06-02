# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        

        def rec(root, curr_path, curr_sum, ret):
            if not root:
                return
            
            new_path = list(curr_path)
            new_path.append(root.val)
            curr_sum += root.val

            if curr_sum == targetSum and not root.left and not root.right:
                ret.append(new_path)
                return
          
            rec(root.left, new_path, curr_sum, ret)
            rec(root.right, new_path, curr_sum, ret)
                
        
        ret = []
        rec(root, [], 0, ret)

        return ret