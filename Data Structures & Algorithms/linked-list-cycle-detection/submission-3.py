# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        if head==None:
            return False
        if head.next==None:
            return False
        while fast!=None:
            slow=slow.next
            if  fast.next!=None:
                fast=fast.next.next
            else:
                fast=None
            if fast==slow:
                return True
        return False

        
        