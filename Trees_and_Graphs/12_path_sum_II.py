'''
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self): 
        self.res = []
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        
        def helper(root, sum, path=[]):
            if root is None: 
                return None 
            if sum - root.val == 0 and root.left is None and root.right is None: 
                self.res.append(path + [root.val])
                return None
            if root.left: 
                helper(root.left, sum-root.val, path+[root.val]) #want to create path dynamically in the recursive function; initilizing a global path (a single list) will be constantly modified even after appending self.res, which creates problems 
            if root.right: 
                helper(root.right, sum-root.val, path+[root.val])
  
         
        helper(root, sum)
        return self.res 
