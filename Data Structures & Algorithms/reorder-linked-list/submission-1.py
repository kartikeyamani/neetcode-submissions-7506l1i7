# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        temp=slow.next
        slow.next=None
        temp2=head
        prev=None
        curr=temp
        while curr:
            temporary=curr.next
            curr.next=prev
            prev=curr
            curr=temporary
        #print(head.val)
        # while prev:
        #     print(prev.val)
        #     prev=prev.next
        curr=head
        while prev:
            temp=curr.next
            curr.next=prev
            curr=prev
            prev=prev.next
            curr.next=temp
            curr=curr.next
        
        



            


        