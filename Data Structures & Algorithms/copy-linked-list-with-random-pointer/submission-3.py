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
        curr=head
        if head==None:
            return None
        temp=None
        h1={}
        while curr:
            newnode=Node(curr.val)
            if temp!=None:
                temp.next=newnode
            temp=newnode
            h1[curr]=newnode
            curr=curr.next
        if temp!=None:
            temp.next=None
        curr=head
        while curr:
            currrandomptr=curr.random
            if currrandomptr!=None:
                currrandomptr=h1[currrandomptr]
            h1[curr].random=currrandomptr
            curr=curr.next
        return h1[head]



        