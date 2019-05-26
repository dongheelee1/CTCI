'''
Find kth to last element of singly linked list. 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        '''
        IDEA: 
        
        have two pointers 
        
        place the first pointer at n+1st node 
        
        then, move up first and second pointers until first is pointing to None 
        '''
        second = first = head 
        
        #decrease n  
        while n > 0: 
            first = first.next 
            n -= 1 

        #at this point first is pointing to n+1 position 
        #until first is pointing to None, increment both pointers  
        while first is not None: 
            first = first.next 
            second = second.next 
        

        return second.val
