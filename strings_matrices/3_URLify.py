'''
Write a method to replace all spaces in a string with %20

You may assume that the string has sufficient space at the end to hold the additional chars 

You are given the "true" length of the string 
'''

def URLify(str): 
  lst = str.strip().split(" ") #convert str to list, splitting on space
  output = "%20".join(lst) #join the contents of the arr 
  return output 
