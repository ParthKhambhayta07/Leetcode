# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, None)
        cur = dummy
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 
            sum = v1 + v2 + carry

            carry = sum // 10

            dummy.next = ListNode(sum % 10, None)
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            dummy.next = ListNode(carry, None)

        return cur.next

        