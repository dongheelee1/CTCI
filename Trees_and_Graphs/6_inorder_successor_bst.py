'''
285. Inorder Successor in BST

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 

Note:

If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.successor = None
        
    def inorderSuccessor(self, root, p):
        
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        def right_child_successor(root): #the right child is passed in 
            
            if root is None: 
                return root #if there is no right child, just return 
            if root.left is None: 
                return root #otherwise, return the last left-child
            return right_child_successor(root.left) #recurse 
            
        def helper(root, lower=None, upper=None): 
            
            if root is None:  
                return None #backtrack 
            
            #when we find the target, do stuff 
            if root is p: 
                #since current node is target p, check to see if it has a successor 
                #pass in current's right child and return the last left-child  
                r = right_child_successor(root.right)
                if root.right: 
                    print(r.val)
                if r:
                    self.successor = r 
                else: #if there isn't a right branch of current, return current's upper bound 
                    self.successor = upper
                return None
            
            #DFS recursion 
            helper(root.left, lower, root)
            helper(root.right, root, upper)
        
        helper(root) #call helper root 
  
        return self.successor
