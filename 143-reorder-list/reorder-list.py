# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        count = 0
        cur = head

        while(cur):
            count+=1
            cur = cur.next
        
        half_count = count//2

        counter = 1
        cur = head
        while(counter<half_count):
            cur = cur.next
            counter+=1
        
        #print(cur)

        rest = cur.next
        cur.next = None

        prev = None
        cur = rest

        while(cur):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        post = prev
        cur = head
        pre = head.next
        while(pre and post):
            cur.next = post
            post = post.next
            cur = cur.next

            cur.next = pre
            pre = pre.next
            cur = cur.next

        if(post):
            cur.next = post

        return head
        

