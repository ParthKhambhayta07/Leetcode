# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        newls = ListNode(0, None)
        cur = newls
        while list1 and list2:
            if list1.val >= list2.val:
                newls.next = ListNode(list2.val, None)
                newls = newls.next
                list2 = list2.next
            else:
                newls.next = ListNode(list1.val, None)
                newls = newls.next
                list1 = list1.next
        
        if list1:
            newls.next = list1
        if list2:
            newls.next = list2

        return cur.next