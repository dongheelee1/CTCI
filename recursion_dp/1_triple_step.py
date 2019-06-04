'''
Recursive Solution 

if n == 0 or n == 1: 
    return 1 
        
return self.climbStairs(n-1) + self.climbStairs(n-2)
'''

'''
DP Solution 

-How to interpret this? 

What are the base cases? 

There is 1 way to climb 0 stairs -- that is, by taking 0 steps 
There is 1 way to climb 1 stair -- that is, by taking 1 step 

There are two ways to climb 2 stairs -- get the # of ways for remaining stairs after taking 1 step: DP[2-1] = DP[1] which has been cached
                                     -- get the # of ways for remaining stairs after taking 2 steps: DP[2-2] = DP[0] which has been cached 
                                     
Generalizing the above, we get DP[i] = DP[i-1] + DP[i-2] 
The number of ways to climb i flight of stairs is to sum the number of ways to climb remaining i-1 stairs after taking a step
and the number of ways to climb i-2 stairs after taking 2 steps 

                                     

    DP = [0 for x in range(0, n+1)]
        
    DP[0] = 1 
    DP[1] = 1
        
    for i in range(2, n + 1): 
            
        DP[i] = DP[i-1] + DP[i-2]
        
    return DP[n]
'''
class Solution:
    
    def climbStairs(self, n: int) -> int:
        
        if n == 0 or n == 1: 
            return 1
        a = 1 #(n-1)
        b = 1 #(n-2)
        output = 0
        for i in range(2, n+1): 
            output = a + b
            b = a 
            a = output
        
        return output
