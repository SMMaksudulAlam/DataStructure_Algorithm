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
        dic = {}
        cur = head
        while(cur):
            node = Node(cur.val)
            dic[cur] = node
            cur = cur.next
        
        cur = head
        dummy = Node(0)
        c = dummy

        while(cur):
            next = None
            random = None
            if(cur.next):
                next = dic[cur.next]
            if(cur.random):
                random = dic[cur.random]
            
            nde = dic[cur]
            nde.next
            nde.random = random

            c.next = nde
            c = c.next

            cur = cur.next
            
        return dummy.next