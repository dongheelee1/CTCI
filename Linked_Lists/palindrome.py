# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

class Solution:
    '''
    complexity: 
    space = O(N)
    time = O(N)
    
    IDEA: 
    
    go through each node in linked list, appending value to stack 
    
    go through each node in linked list again, pop value from stack, and compare 
    
        if values don't match, return False 
    
    return True if there is no issue in above loop
    '''
    def isPalindrome(self, head: ListNode) -> bool:
        
        stack = [] 
        
        current = head 
        
        while current: 
            stack.append(current.val)
            current = current.next 
        
        
        while stack: 
            
            pop = stack.pop()
            
            if head.val != pop: 
                return False
            
            head = head.next 
            
        return True 
