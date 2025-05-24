# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        stack = []
        length = 0
        while head:
            stack.append(head.val)
            head = head.next
            length +=1 
        
        for i in range(length // 2):
            if stack.pop() != stack[i]:
                return False
        
        return True