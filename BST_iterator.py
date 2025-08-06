# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        
        self.inOrder = []
        stack = []
        curr = root

        while curr is not None or len(stack) > 0:
            
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            self.inOrder.append(curr.val)

            curr = curr.right
        
        self.idx = 0

    def next(self):
        """
        :rtype: int
        """
        
        ret = self.inOrder[self.idx]
        self.idx += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.idx < len(self.inOrder):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()