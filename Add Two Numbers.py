# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        remainder = 0
        dummy = ListNode()
        current = dummy

        while(l1 and l2):
            sum = l1.val + l2.val

            if(remainder > 0):
                sum = sum + remainder
                remainder = 0            

            if (sum//10 > 0):
                remainder = sum//10
            
            current.next = ListNode(sum%10)
            current = current.next
            
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val

            if(remainder > 0):
                sum = l1.val + remainder
                remainder = 0            

            if (sum//10 > 0):
                remainder = sum//10
            
            current.next = ListNode(sum%10)
            current = current.next
            
            l1 = l1.next

        while l2:
            sum = l2.val
            if(remainder > 0):
                sum = l2.val + remainder
                remainder = 0            

            if (sum//10 > 0):
                remainder = sum//10
            
            current.next = ListNode(sum%10)
            current = current.next
            
            l2 = l2.next
        
        if remainder:
            current.next = ListNode(remainder)
            current = current.next
            
        return dummy.next
        
