'''
Delete a node in the middle (i.e. any node but the first and last node, not necessarily the exact middle of a singly linked list, given only access to that node. 
'''

class Solution:
    def deleteNode(self, node):
        """ 
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val = node.next.val #replace value of current node to be value of current node's next 
        node.next= node.next.next #current node's next is set to current node's next.next
