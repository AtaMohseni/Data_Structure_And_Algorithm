# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:39:49 2021

@author: ATA
"""

def brute_force(text,pattern):
    """ if find pattern in the text, return the first occurance of pattern in the text"""
    """ best case: O(n) when pattern is not found and the first character in pattern
    is not existed in text"""
    """ worst case O(m * (n-m+1)) when only the last character is different"""
    l1 = len(text)
    l2 = len(pattern)
    
    i = 0           # looping variable over text positions which patern starts
    j = 0           # looping variable over patern character
    flag = False    # if pattern doesnt found, it print the pattern is not present (last if statement)
    
    while i < l1:   # iteration from 0th index of text
        j = 0
        count = 0 # count stores the length up to which the pattern and text have matched
        
        while j < l2:
            if i+j < l1 and text[i+j] == pattern[j]:
                count += 1
                
            j += 1
                
        if count == l2: #it shows pattern is found in the text
            print("\nPettern occures at index ",i)
            flag =True
        i += 1
        
    if not flag:
        print("\nPattern is not exist in text")
        
if __name__ == "__main__":  
        
    brute_force("abcdefgh","gh")
            
                    