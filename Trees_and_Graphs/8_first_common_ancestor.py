'''
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self): 
        self.answer = None 
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def lca(root): 
            
            #return False when we've reached the end of the branch 
            if root is None: 
                return False # 

            l = lca(root.left)
            r = lca(root.right)

            m = root == p or root == q #if root is either p or q 

            if m + l + r >= 2: #we know that we have LCA if p and q exists in l and r (then lca is m); it could also be m and r or m and l, in which case still return m  
                self.answer = root 

            return m or l or r #return True (bubble up the flags) if any of the three bool values is True. 
        
        lca(root) #lowestCommonAncestor calls lca to get self.answer 
        return self.answer
