# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=0
        while curr!=None:
            count=count+1
            curr=curr.next
        front=count-n
        curr=head
        if(front==0):
            return curr.next
        while front>1:
            curr=curr.next
            front=front-1
        curr.next=curr.next.next
        return head
        
        