# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_dummy = ListNode()
        curr = sum_dummy

        carry = 0
        while l1 or l2:
            digit_sum = carry

            if not l1:
                digit_sum += l2.val
                l2 = l2.next
            elif not l2:
                digit_sum += l1.val
                l1 = l1.next
            else:
                digit_sum += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next

            if digit_sum >= 10:
                carry = 1
                digit_sum -= 10
            else:
                carry = 0

            curr.next = ListNode(digit_sum)
            curr = curr.next

        if carry != 0:
            curr.next = ListNode(carry)

        return sum_dummy.next
