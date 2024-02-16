# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        sum_list_head = None
        sum_list_current = None        

        carry = 0

        while (l1 != None or l2 != None):
            l1val = 0
            l2val = 0

            if (l1 != None):
                l1val = l1.val
                l1 = l1.next

            if (l2 != None):
                l2val = l2.val
                l2 = l2.next

            digit_sum = l1val + l2val + carry
            if (digit_sum > 9):
                digit_sum = digit_sum % 10
                carry = 1
            else:
                carry = 0

            if (sum_list_head == None):
                sum_list_head = ListNode(digit_sum)
                sum_list_current = sum_list_head
            else:
                sum_list_current.next = ListNode(digit_sum)
                sum_list_current = sum_list_current.next

        if (carry > 0):
            sum_list_current.next = ListNode(1)

        return sum_list_head
