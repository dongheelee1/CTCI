'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other. 
'''
def check_permuation(str1, str2): 
  if sorted(str1) == sorted(str2): 
    return True 
  return False 

