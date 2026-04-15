# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q=0
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2 or q:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            t = val1 + val2 + q
            r = t%10
            q = t//10
            cur.next=ListNode(r)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        if q > 0:
            cur.next = ListNode(q)
        return dummy.next
