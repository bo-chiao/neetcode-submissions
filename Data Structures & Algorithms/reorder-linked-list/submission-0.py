# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return
        # 1. find mid
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        # 2. reverse the second half
        prev, curr = None, mid
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # 3. merge two halfs
        tail = prev
        while tail.next:
            head.next, tail.next, head, tail = tail, head.next, head.next, tail.next
