# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 0
        cur = dummy = head

        if n == 0: 
            return head

        while dummy:
            index = index + 1
            dummy = dummy.next
        
        if index == 1:
            return None
        elif index == n:
            return head.next
        else:
            while cur:
                if index - 1 == n:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
                index = index - 1
        
        return head