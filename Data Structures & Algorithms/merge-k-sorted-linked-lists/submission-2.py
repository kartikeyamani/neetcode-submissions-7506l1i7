# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists)==0:
            return None
        
        while len(lists)>1:
            head1=lists[0]
            head2=lists[1]

            dummy=ListNode()
            curr=dummy
            while head1 and head2:
                if head1.val<=head2.val:
                    dummy.next=head1
                    head1=head1.next
                else:
                    dummy.next=head2
                    head2=head2.next
                dummy=dummy.next
            if head1:
                dummy.next=head1
            if head2:
                dummy.next=head2
            lists.pop(0)
            lists.pop(0)
            lists.insert(0,curr.next)
        return lists[0]
            


        