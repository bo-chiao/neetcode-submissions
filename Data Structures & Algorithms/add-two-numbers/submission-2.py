# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = ListNode()
        helper = previous_node
        
        carry = 0

        while l1 or l2 or carry:
            digit_sum = carry

            digit_sum += l1.val if l1 else 0
            digit_sum += l2.val if l2 else 0

            digit = digit_sum % 10
            carry = digit_sum // 10

            current_node = ListNode(digit)
            previous_node.next = current_node
            previous_node = previous_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return helper.next
        