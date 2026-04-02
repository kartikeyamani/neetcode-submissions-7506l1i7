# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        while len(lists)>1:
            l1=lists[0]
            l2=lists[1]
            dummy=curr=ListNode()
            while l1!=None and l2!=None:
                if l1.val<=l2.val:
                    dummy.next=l1
                    l1=l1.next
                    dummy=dummy.next
                    dummy.next=None
                else:
                    dummy.next=l2
                    l2=l2.next
                    dummy=dummy.next
                    dummy.next=None
            if l1!=None:
                dummy.next=l1
            if l2!=None:
                dummy.next=l2
            lists.pop(0)
            lists.pop(0)
            lists.insert(0,curr.next)
        return lists[0]

        