"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        def rec(root, level, ret):

            if not root:
                return
            
            if level <= len(ret):
                ret.append([])

            ret[level].append(root)

            rec(root.left, level+1, ret)
            rec(root.right, level+1, ret)
        

        ret = []

        rec(root, 0, ret)

        for level in ret:
            for i in range(0, len(level)-1):
                level[i].next = level[i+1]
                
        if ret:
            return ret[0][0]
        return None