# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        firsttime=1
        newhead=None
        beforeprev=None
        while True:
            curr=head
            count=0
            first=head
            last=head
            while curr!=None and count!=k:
                count+=1
                last=last.next
                curr=curr.next
            if curr==None and count<k:
                break
            curr=first
            prev=None
            while curr!=last:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            first.next=curr
            head=head.next
            if firsttime==1:
                newhead=prev
                firsttime=0
                beforeprev=first
            else:
                beforeprev.next=prev
                beforeprev=first
        return newhead




        
        

        