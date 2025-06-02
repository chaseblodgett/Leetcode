# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        
        def rec(nums):
            if nums:
                mid = len(nums) // 2
                root = TreeNode(nums[mid])

                root.left = rec(nums[:mid])
                root.right = rec(nums[mid+1:])

                return root

            return None
            
        if not head:
            return None

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return rec(nums)