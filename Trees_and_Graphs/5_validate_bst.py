# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
    
    5
   / \
  1   6
     / \
    3   9

The above example is not a BST. 
'''
class Solution(object):
    '''
    Wrong idea: 
    
    Comparing the current node with respect to left and right children is WRONG. 
    
    Take below tree as an example. 3 has to be greater than 5, less than 6. 
    
    Given this, keep track of an upper and lower limit. 

        5
       / \
      1   6
         / \
        3   9
    Correct Idea: 
    
    At every level of the function call (going top down), check that the root's value is within the bounds. 
    
    If not, return False 
    
    Then, go deeper down the tree by recursively calling helper function on...
        root.left, passing in upper = root.val, lower stays the same 
        and then, 
        root.right, passing in upper stays the same, lower = root.val 
        
     If any of these calls returns False / not True, return False 

     Otherwise, return True. 

    '''
    import sys 
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def isValidBST_helper(root, lower=-sys.maxsize, upper=sys.maxsize): 
            
            if root is None: 
                return True 

            if root.val <= lower or root.val >= upper: #when root value is out of bounds, then return False 
                return False
            
            if not isValidBST_helper(root.left, lower, root.val): #check if left branch is a valid BST, keeping lower bound the same and setting upper bound as root.val
                return False 
            
            if not isValidBST_helper(root.right, root.val, upper): #check if right branch is a valid BST, keeping upper bound the same and setting lower bound as the root.val
                return False 
            
            return True 
        
        return isValidBST_helper(root)
            
