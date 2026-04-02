# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rec(self,head,l):
        if head==None:
            return None
        
        head.next=self.rec(head.next,l)
        l[0]-=1
        if l[0]==0:
            return head.next
        return head
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # total=0
        # curr=head
        # while curr:
        #     total+=1
        #     curr=curr.next
        # if total==n:
        #     return head.next
        # total=total-n
        # curr=head
        # while total>1:
        #     total-=1
        #     curr=curr.next
        # curr.next=curr.next.next
        # return head

        return self.rec(head,[n])

    
        


        