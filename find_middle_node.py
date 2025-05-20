# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        arr = []
        curr = head
        i = 0

        while curr:
            curr = curr.next
            i += 1
        
        for i in range(int(math.ceil(i / 2))):
            head = head.next
        
        return head