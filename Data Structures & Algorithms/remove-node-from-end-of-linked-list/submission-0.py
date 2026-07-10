# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, slow, fast = dummy, head, head
        for _ in range(n - 1):
            fast = fast.next

        while fast.next:
            prev, slow, fast = slow, slow.next, fast.next

        prev.next = slow.next

        return dummy.next
