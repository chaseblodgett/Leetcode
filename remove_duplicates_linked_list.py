# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head:
            curr = head.next
            prev_val = head.val
            prev_diff_node = head
        else:
            return head
        
        while curr:
            if prev_val != curr.val:
                print(prev_val)
                print(curr.val)
                prev_diff_node.next = curr
                prev_diff_node = prev_diff_node.next
            else:
                prev_diff_node.next = None
            
            prev_val = curr.val
            curr = curr.next

        return head
