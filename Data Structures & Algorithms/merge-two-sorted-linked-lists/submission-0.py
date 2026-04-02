# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        l1=list1
        l2=list2
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                curr.next=l1
                curr=curr.next
                l1=l1.next
                curr.next=None
            else:
                curr.next=l2
                curr=curr.next
                l2=l2.next
                curr.next=None
            
        while l1!=None:
            curr.next=l1
            curr=curr.next
            l1=l1.next
            curr.next=None
        while l2!=None:
            curr.next=l2
            curr=curr.next
            l2=l2.next
            curr.next=None
        return dummy.next
        



        