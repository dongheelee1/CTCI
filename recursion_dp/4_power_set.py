'''
78. Subsets


Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
[[]]
[[], [a]] #newly added 
[[], [a], [b], [a, b]] #newly added: [b], [a, b]
[[], [a], [b], [a, b], [c], [a, c], [b, c], [a, b, c]] #newly added: [c], [a, c], [b, c], [a, b, c]

IDEA: 

1. the result set has an empty set to start 
2. iterate through the given numbers list and add the current number to each item in the result set
3. add the new list of items to the result set 
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        

        #iterative solution 
        
        res = [[]] #start with the empty set 
        for num in nums:
            print(num)
            res += [item+[num] for item in res]
        return res

    
