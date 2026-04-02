# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr=head
        length=0
        while curr!=None:
            curr=curr.next
            length=length+1
        half_length=length//2
        curr=head
        while half_length>1:
            half_length=half_length-1
            curr=curr.next
        new_list=None
        if curr!=None and curr.next !=None:
            new_list=curr.next
            curr.next=None
        ## Reversing the second half of the list
        if new_list!=None:
            prev=None
            curr=new_list
            while curr!=None:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            curr=head
            while curr!=None and prev!=None:
                temp1=curr.next
                if temp1==None:
                    curr.next=prev
                    break
                curr.next=prev
                temp2=prev.next
                prev.next=temp1
                prev=temp2
                curr=temp1
            



            

        