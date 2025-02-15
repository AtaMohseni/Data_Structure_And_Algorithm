# -*- coding: utf-8 -*-
"""
Created on Sat May 29 13:00:20 2021

@author: ATA
"""
def linear_search_orderedinput(ordered_list,term):
    for i in range(len(ordered_list)):
        if term == ordered_list[i]:
            return i
        elif ordered_list[i] > term:
            return None
        
def binary_search_iterative(ordered_list,term):
    """Input should be an ascending ordered list """
    """ O(log n)"""
    index_of_first_element = 0
    index_of_last_element = len(ordered_list) - 1
    
    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element) // 2
        
        if ordered_list[mid_point] == term:
            return mid_point
        
        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1
    # case which input list is empty        
    if index_of_first_element > index_of_first_element:
        return None
    
    
def binary_search_recurive(ordered_list,first_element_index,last_element_index,term):
    """ Input should be an ascending ordered list"""
    """ O(log n)"""
    
    #base Case:
    if (last_element_index < first_element_index):
        return None
    #recursion:
    else:
        midpoint = first_element_index +((last_element_index - first_element_index) // 2)
        
        if ordered_list[midpoint] > term:
            return binary_search_recurive(ordered_list,first_element_index,midpoint-1,term)
        elif ordered_list[midpoint] < term :
            return binary_search_recurive(ordered_list, midpoint + 1,last_element_index,term)
        else:
            return midpoint
        
def interpolation_search (ordered_list, term):
    """ same implementation as binary_search_iterative, but mid point is choosen
    differently in every step, according to linearly ascending equation of line"""
    
    index_of_first_element = 0
    index_of_last_element = len(ordered_list) - 1
    
    
    while index_of_first_element <= index_of_last_element:
        
        mid_point = index_of_first_element + ((index_of_last_element-index_of_first_element)//(ordered_list[index_of_last_element]-ordered_list[index_of_first_element]))* (term - ordered_list[index_of_first_element])
        
        #case which our serach element is not in list bc it is either
        #larger than last element of list,or smaller than first element of list 
        if mid_point > index_of_last_element or mid_point < index_of_first_element:
            return None
        
        if ordered_list[mid_point] == term:
            return mid_point
        
        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1
            
    # case which input list is empty      
    if index_of_first_element > index_of_first_element:
        return None


if __name__ == "__main__" :
    
    lst = [2,4,5,12,60,60,60,77,88,89,90]
    search_number = 60
    print("ordered linear search:",linear_search_orderedinput(lst,search_number))
    print("iterative binary search:",binary_search_iterative(lst,search_number))
    print('recurive binary search:',binary_search_recurive(lst,0,len(lst)-1,search_number))
    print('interpolation search:',interpolation_search(lst,search_number))