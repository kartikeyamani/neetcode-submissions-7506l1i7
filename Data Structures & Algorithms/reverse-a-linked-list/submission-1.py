# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        curr=head.next
        truehead=head
        temp=None
        while curr:
            temp=curr.next
            curr.next=head
            head=curr
            curr=temp
        truehead.next=temp
        return head
            


        