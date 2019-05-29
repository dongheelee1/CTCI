'''
Implement a function to check if a binary tree is balanced. 
For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''
'''
IDEA: 

A balanced binary tree has to fulfill 3 things: 

1. the difference in height of the left and right subtrees must be at most 1 
2. left subtree must be balanced 
3. right subtree must be balanced 

height = longest path (count # of edges) from root to leaf 

isBalanced(root)
    [1] if root is None <-- trivially, the tree is balanced 
    
    [2] calculate height difference between root's left and root's right 
    
    [3] if greater than 1, return False 
    
    [4] otherwise, check that both left and right subtrees are balanced 
    
getHeight(root):     
    an empty tree has 0 height so if this is the case, return 0 
    
    *don't account for tree with 1 node (height = 0) in this problem as isBalanced takes care of it in [2]
    
    otherwise, return 1 + max(getHeight(left), getHeight(right))
    
    
'''

class Solution(object):
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None: 
            return True  #base case for isBalanced, when the root is None, it's always balanced 
    
        if abs(self.getHeight(root.left) - self.getHeight(root.right)) > 1: 
            return False 
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    
    
    def getHeight(self, root): 
        
        if root is None: 
            return 0 #a tree with 0 nodes has 0 height 
 
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
