# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:34:33 2021

@author: ATA
"""
#########################################Book Method
def pfun(pattern):          # function to generate prefix function for the given pattern
    """O(m) where m in length of pattern"""
    n = len(pattern)        # length of the pattern
    prefix_fun = [0]*(n)    # initialize all elements of the list to 0
    k = 0
    for q in range(2,n):
        while k>0 and pattern[k+1] != pattern[q]:
            k = prefix_fun[k]
        if pattern[k+1] == pattern[q]:      # If the kth element of the pattern is equal to the qth element
            k += 1                          # update k accordingly
        prefix_fun[q] = k
    return prefix_fun                       # return the prefix function




print("pfun result:",pfun("-acacac"))


def KMP_Matcher(text,pattern):              # KMP matcher function
    """O(n) where n is length of text"""
    m = len(text)
    n = len(pattern)
    flag = False
    text = '-' + text                       # append dummy character to make it 1-based indexing
    pattern = '-' + pattern                 # append dummy character to the pattern also
    prefix_fun = pfun(pattern)              # generate prefix function for the pattern
    q = 0
    for i in range(1,m+1):
        while q>0 and pattern[q+1] != text[i]:      # while pattern and text are not equal, decrement the value of q if it is > 0
            q = prefix_fun[q]
        if pattern[q+1] == text[i]:                 # if pattern and text are equal, update value of q
            q += 1
        if q == n:                                      # if q is equal to the length of the pattern, it means that the pattern has been found.
            print("Pattern occours with shift",i-n)     # print the index, where first match occours.
            flag = True
            q = prefix_fun[q]
    if not flag:
        print('\nNo match found')

KMP_Matcher('acacabacababacacac','acacac')              # function call, with two parameters,text and pattern


################################################## Internet Method:
# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
  
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            print ("Found pattern at index " + str(i-j))
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
  
def computeLPSArray(pat, M, lps):
    length = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if length != 0:
                length = lps[length-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
                
if __name__ == "__main__": 
    
    txt = "acacabacababacacac"
    pat = "acacac"
    KMPSearch(pat, txt)