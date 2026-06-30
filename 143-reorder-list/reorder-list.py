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

        dummyNode = ListNode()
        dummyNode.next = head

        length = 0
        current = dummyNode
        while(current != None):
            length += 1
            current = current.next

        #print(length)

        half = length//2

        firstHalf = head
        secondHalf = None

        count = 0
        current = dummyNode
        while(count < half):
            current = current.next
            count+=1
        
        secondHalf = current.next
        current.next = None

        #print(firstHalf, secondHalf)

        prev = None
        while(secondHalf):
            next = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = next

        secondHalf = prev
        #print(firstHalf, secondHalf)
        
        current = head
        while(secondHalf):
            next = current.next
            current.next = secondHalf
            #print(secondHalf)
            secondHalf = secondHalf.next
            current = current.next
            current.next = next
            current = current.next
        
        
