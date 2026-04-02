# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode()
        curr=dummy
        while l1!=None and l2!=None:
            new_num=l1.val+l2.val+carry
            carry=new_num//10
            new_num=new_num%10
            curr.next=ListNode(new_num)
            curr=curr.next
            l1=l1.next
            l2=l2.next
        while l1!=None:
            new_num=l1.val+carry
            carry=new_num//10
            new_num=new_num%10
            curr.next=ListNode(new_num)
            curr=curr.next
            l1=l1.next
        while l2!=None:
            new_num=l2.val+carry
            carry=new_num//10
            new_num=new_num%10
            curr.next=ListNode(new_num)
            curr=curr.next
            l2=l2.next
        if carry>0:
            curr.next=ListNode(carry)
        return dummy.next



        