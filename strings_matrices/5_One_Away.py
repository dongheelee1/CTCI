
#A and B are strings
#return True if A and B are one or zero edits away (there can be insert a char, remove a char, or replace a char)
def one_away(A, B): 
        lengths_differ_by_one = False 
        edits = 0  
        
        if abs(len(B) - len(A)) > 1: 
            return False 
        elif abs(len(B) - len(A)) == 1: 
            lengths_differ_by_one = True
        elif abs(len(B) - len(A)) == 0: 
            lengths_differ_by_one = False
        
        #string lengths differ, check if there is an insertion/delete
        if lengths_differ_by_one: 
            while i < len(A) and j < len(B): 
                if A[i] != B[i]: 
                    edits += 1
                    if edits > 1: 
                        return False
                    if len(A) > len(B): 
                        i += 1 #just move pointer for A 
                    else: 
                        j += 1 #just move pointer for B 
                else: 
                    #if chars match, move both pointers
                    i += 1 
                    j += 1
                
        #string lengths don't differ --> possible replacement
        else: 
            for i in range(len(A)): 

                if A[i] != B[i]: 

                    edits += 1 

                    if edits > 1: 
                        return False    
        return True 
