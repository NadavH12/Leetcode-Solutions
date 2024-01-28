# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        pointer = head
        delay_pointer = head
        
        i = 0
        while(pointer != None):
            pointer = pointer.next
            if (i - n > 0):
                delay_pointer = delay_pointer.next
            i += 1

        #special case to remove first node
        if (n == i):
            head = head.next
        elif (delay_pointer.next != None):
            delay_pointer.next = delay_pointer.next.next

        return head
