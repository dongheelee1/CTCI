'''
86. Partition List
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



'''
iterate through linked list and populate 'before' and 'after' LLs based on given x 
merge 'before' and 'after' LLs and return the before_head

Time Complexity - O(N) (1 while loop)
Space Complextiy - O(1) (not using any extra space )
'''



class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        if head is None: 
            return None 
        
        #before_head and before pointers initialized with dummy nodes 
        before_head = before = ListNode(None)
        after_head = after = ListNode(None)
        
        #iterate thorugh the given linked list and append each value to either 'after' LL or 'before' LL 
        while head: 
            
            #if current node's val is less than the given x (aka pivot), append to 'before' LL
            if head.val < x: 
                before.next = head 
                before = before.next #increment the 'before' pointer
            #if current node's val is greater than the given x (aka pivot), append to 'after' LL 
            elif head.val >= x: 
                after.next = head 
                after = after.next #increment the 'after' pointer
                
            head = head.next #increment the head pointer 
        
        after.next = None 
        before.next = after_head.next #merge 'before' and 'after' LLs
        before_head = before_head.next 
        
        return before_head
