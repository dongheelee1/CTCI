'''
73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Time - O(M*N)
Space - O(1)
'''

'''
IDEA: 
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        cols_zero = False 
        rows_zero = False 
        
        #check to see if there is 0 exists in the 0th row
        #if it does, make note and break
        for i in range(cols): 
            if matrix[0][i] == 0: 
                cols_zero = True 
                break 
        
        #check to see if there is 0 exists in the 0th col
        #if it does, make note and break
        for i in range(rows): 
            if matrix[i][0] == 0: 
                rows_zero = True 
                break 
        
        #start at the 1st col and 1st row, and iterate
        #if you encounter a 0, indicate 0 on the 0th row and 0th col cells that intersect with current cell
        for row in range(1, rows): 
            for col in range(1, cols): 
                if matrix[row][col] == 0:
                    matrix[0][col] = 0 
                    matrix[row][0] = 0 
                    
        #iterate through the same matrix again       
        #if matrix[0][col] is 0 or if matrix[row][0] is 0, make the current cell 0    
        for row in range(1, rows): 
            for col in range(1, cols): 
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0 
        
        # See if the 0th column and 0th row needs to be set to zero as well             
        if cols_zero: 
            for i in range(cols): 
                matrix[0][i] = 0
                
        if rows_zero: 
            for j in range(rows):
                matrix[j][0] = 0 
            
                     
