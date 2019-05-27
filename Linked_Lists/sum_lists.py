'''
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        IDEA (BUT REFACTOR THIS CODE!!!!): 
        
        initialize a carry variable with value 0 
        
        go ahead and add l1 and l2 node by node and carry 
        
        if sum is greater than 10, subtract 10 and make note of digit append 
        
        if sum is less than 10, make note of digit and reset carry to 0 
        
        append ListNode(digit) to result 
        
        increment l1, l2, and result counters 
        
        
        if l1 and l2 doesn't exist, but carry exists, append ListNode(carry) to result 
        otherwise: 
            repeat similar step for if l1 still exists (length is greater than l2)
            repeat similar step for if l2 still exists (length is greater than l1)
        '''
        result = result_head = ListNode(None)
        carry = 0
        
        while l1 and l2: 
            
            digit_sum = l1.val + l2.val + carry 
            
            if digit_sum >= 10: 
                
                digit = digit_sum - 10 
                
                carry = 1 
                
            else: 
                
                digit = digit_sum 
                carry = 0
                
            result.next = ListNode(digit) 
            
            l1 = l1.next 
            l2 = l2.next 
            result = result.next
            
        if l1 is None and l2 is None and carry:   
            result.next = ListNode(carry)
        else: 
            while l1: 

                digit_sum = l1.val + carry 

                if digit_sum >= 10: 

                    digit = digit_sum - 10 

                    carry = 1 

                else: 

                    digit = digit_sum 
                    carry = 0 

                result.next = ListNode(digit) 

                l1 = l1.next 
                result = result.next

            while l2: 
                digit_sum = l2.val + carry 

                if digit_sum >= 10: 

                    digit = digit_sum - 10 

                    carry = 1 

                else: 

                    digit = digit_sum 
                    carry = 0 

                result.next = ListNode(digit) 

                l2 = l2.next 
                result = result.next
        
            
        return result_head.next
            

 
    '''
    ANALYZE this leetcode solution: 
    
       def addTwoNumbers(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next
    '''
