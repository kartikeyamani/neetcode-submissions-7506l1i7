# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        curr=l1
        l1length=0
        while curr:
            l1length+=1
            curr=curr.next
        curr=l2
        l2length=0
        while curr:
            l2length+=1
            curr=curr.next
        curr1,curr2=l1,l2
        if l1length<l2length:
            curr1,curr2=curr2,curr1
        prev=None
        while curr1 and curr2:
            newsum=curr1.val+curr2.val+carry
            carry=int(newsum/10)
            newsum=newsum%10
            curr1.val=newsum
            prev=curr1
            curr1=curr1.next
            curr2=curr2.next
        while curr1!=None:
            newsum=curr1.val+carry
            carry=int(newsum/10)
            newsum=newsum%10
            curr1.val=newsum
            prev=curr1
            curr1=curr1.next
        if carry!=0:
            newnode=ListNode(carry)
            prev.next=newnode
        if l2length>l1length:
            return l2
        return l1


        
        

        


        