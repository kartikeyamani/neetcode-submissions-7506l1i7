"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newdict={}
        if head==None:
            return None
        curr=head
        while curr:
            newnode=Node(curr.val)
            newdict[curr]=newnode
            curr=curr.next
        curr=head
        while curr:
            newnode=newdict[curr]

            if curr.next:
                newnode.next=newdict[curr.next]
            else:
                newnode.next=None
            if curr.random:

                newnode.random=newdict[curr.random]
            else:
                newnode.random=None
            curr=curr.next
        return newdict[head]
        