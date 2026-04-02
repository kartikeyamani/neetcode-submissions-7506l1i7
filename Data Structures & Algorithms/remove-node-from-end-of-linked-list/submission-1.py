# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        n1=count-n
        if n1==0:
            return head.next
        curr=head
        while n1>1:
            curr=curr.next
            n1-=1
        temp=curr.next
        curr.next=temp.next
        del temp
        return head
        
        
        
        
        

        