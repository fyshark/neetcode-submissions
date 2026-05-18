# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        res = dummy

        for i in range(n):
            head = head.next
        
        while head:
            res = res.next
            head = head.next
        
        res.next = res.next.next
        return dummy.next