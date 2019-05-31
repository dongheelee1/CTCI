'''
Algorithm to determine if a sring has all unique characters. What if you cannot use additional data structures?
'''
'''
IDEA: 

sort the string 

check to see if current char is the same as the char after 

if so, return False (string not unique)
if not, continue in for loop 

Note: string is converted to arr 
'''

def is_unique(arr): 
  for i in range(0, len(arr) - 1): 
    if arr[i] == arr[i+1]: 
      return False
    else: 
      return True 
