'''
**Do this linked list version? 
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
IDEA: 

Initialize 

res = []

and define "helper" function that will take in root and level (0, 1, 2, ...)

helper function: 
    if root is None, backtrack 

    otherwise, 

    if the current level is equal to the length of the res list
    then append an empty list to the res

    ^In other words, if there is no list initialized in res at the current level, which serves as index of res, initialize an empty list 

    append actual val to the list 

    recurse on root.left, level+1 
    recurse on root.right, level+1
    
call helper function with root as input    
return res 
'''
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        
        if root is None: 
            return res 
        
        def helper(root, level=0):
            #keep track of depth 
 
            if not root: 
                return None
        
            if level == len(res): 
                #if no list is initialized at the given level, add empty list
                res.append([])

            res[level].append(root.val)
        
            helper(root.left, level+1)
            helper(root.right, level+1)
        
        helper(root)
        return res
        
