# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:34:49 2021

@author: ATA
"""

def median_of_medians(elems):
    """ elems is an arbitrary list, this function return median of medians,
    by recursivly divide elems into 5-element lists, sort them and find their medians,
    again divide these medians into 5-element list of medians, and so on. when 
    the final list in recutsion has 5 elements, mainly 5 medians, it return the
    median value of these 5 elements"""
    
    sublists = [elems[j:j+5] for j in range(0,len(elems),5)]
    medians = []
    for sub in sublists:
        medians.append(sorted(sub)[len(sub)//2])
    
    if len(medians) <=5 :
        return sorted(medians)[len(medians)//2]
    else:
        return median_of_medians(medians)
        
    
def get_index_of_nearest_median(array_list, first,second,median):
    if first == second:
        return first
    else:
        return first + array_list[first:second].index(median)
    
def swap(array_list,first,second):
    """ function to swap emelement in first provided index with element 
    in second provided index"""
    temp = array_list[first]
    array_list[first] = array_list[second]
    array_list[second] = temp
    
def partition(unsorted_array, first_index, last_index):
    if first_index == last_index:
        return first_index
    else:
        nearest_median = median_of_medians(unsorted_array[first_index:last_index])
    
    index_of_nearest_median = get_index_of_nearest_median(unsorted_array, first_index, last_index, nearest_median)
    
    swap(unsorted_array,first_index,index_of_nearest_median)
    
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    
    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index +1 
    
    while True:
        
        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        
        while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1
            
        if greater_than_pivot_index < less_than_pivot_index:
            temp = unsorted_array[greater_than_pivot_index]
            unsorted_array[greater_than_pivot_index] = unsorted_array[less_than_pivot_index]
            unsorted_array[less_than_pivot_index] = temp
        else:
            break
        
    unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index] = pivot
    
    return less_than_pivot_index

def deterministic_select(array_list,left,right,k):
    """determistic function to fund k th smallest element in unsorted array.
    it calls deterministic because we chose pivot as median in every list or sublist
    in every recursuive step.
    Note that k th smallest elemetn will be in k-1 index of final sorted array"""
    """worst case O(n)"""
    split = partition(array_list,left,right)
    
    if split == k:
        return array_list[split]
    elif split < k :
        return deterministic_select(array_list, split + 1, right, k)
    else:
        return deterministic_select(array_list, left, split - 1, k)
    
if __name__ == "__main__":  
    
    lst = [5,8,3,9,1,4,2,6,7,10]
    # to return 5th smallest element: input should be 4
    k_th_smallest_element = 5
    index_of_k_th_smallest_element = k_th_smallest_element - 1
    print(deterministic_select(lst, 0, len(lst)-1, index_of_k_th_smallest_element))
    import random
    import time
    # list of size 1000 incliude integers from 1 to 1e6
    lst= random.sample(range(1, int(1e7)), int(1e6))
    k_th_smallest_element = (len(lst)//4) * 3
    index_of_k_th_smallest_element = k_th_smallest_element - 1
    print("time to find kth smallest element using deterministic_select")
    t1 = time.time()
    print(deterministic_select(lst, 0, len(lst)-1, index_of_k_th_smallest_element))
    print(time.time() - t1)