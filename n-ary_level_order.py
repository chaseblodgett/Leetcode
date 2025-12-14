"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        
        def traverse(node, ret, level):

            if not node:
                return
            
            if level >= len(ret):
                ret.append([])
            
            ret[level].append(node.val)
            for child in node.children:
                traverse(child, ret, level+1)
            
            return ret
        
        if not root:
            return []
        
        return traverse(root, [], 0)