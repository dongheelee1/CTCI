'''
572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
IDEA: 

isSubtree(s, t) method: 
  when tree A is empty, return False (no tree B could be a subset of tree A)
  when tree B is empty, return True (an empty tree B is always a subset of tree A) 

  if both trees exist, then check if tree rooted at A is identical to tree rooted at B (isIdentical(A, B)) 
    if true, return true 

    if false, search identical trees in the left branch of A, search identical trees in the right branch of A. 
    if one of these is true, return true. 
    
    
ifIdentical(s, t) method: 
  if both trees are None, return True*
  *^this can never be hit in the first call of isIdentical since condition is that both s and t exist in isSubtree
  *implies that this is the base case --> reached end of s and t at the same time 
  
  if only one of the trees is None, return False (trees are not identical)
  
  then, 3 things to check: 
  - current nodes s and t are identical 
  - s's left subtree and t's left subtree are identical 
  - s's right subtree and t's right subtree are identical 
  
'''
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None: #if tree is empty 
            return False 
        if t is None: #if subtree is empty, return True because an empty tree is always a subtree
            return True 
        
        if self.isIdentical(s, t): #if both trees exist and (if the tree rooted at s is identical to tree rooted at t)
            return True 
        else: #in the case that tree rooted at s is not identical to tree rooted at t
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) #check if there is an identical tree (subtree) in left branch
                                                                           #check if there is an identical tree (subtree) in right branch 
    def isIdentical(self, s, t): #sub function called in isSubtree 
        if s is None and t is None: #if both trees are None, return True (this can never be hit in the first call of isIdentical since condition is that both s and t exist in isSubtree
            return True 
        if s is None or t is None: #if only one of the trees is None, return False (trees are not identical)
            return False 
        return s.val == t.val and self.isIdentical(s.left, t.left) and self.isIdentical(s.right, t.right)
        #^3 things to check: s and t nodes have the same values, left subtree of s and left subtree of t are identical, right subtree of s and right subtree of t are identical 
        
