# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:18:15 2021

@author: ATA
"""

def partition(unsorted_array,first_index,last_index):
    """ function to be used in QuickSort algorithm. this function assumes the 
    first_index is pivot and move it to differnt location which makes the list into two partions
    such that element of left partion are less then pivot, and elements of 
    right partition are larger than pivot. it return the index of pivot"""
    """ O(n)"""
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    
    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1
    
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

def quick_select(array_list,left,right,k):
    """ Also refer to as Randomize selection because the pivot point is 
    chosen as 1st element of list or sublists (which is a random nnumber) in 
    every recursive step """
    """ worst case is O(n^2)"""
    """ to return k th smallest element: input should be k-1. 
    be caerful, 1 st smallest value has index 0"""
    split = partition(array_list, left, right)
    if split == k:
        return array_list[split]
    elif split < k:
        return quick_select(array_list,split + 1 , right, k)
    else:
        return quick_select(array_list, left, split - 1, k)
    
if __name__ == "__main__":      
    
    lst = [5,8,3,9,1,4,2,6,7,10]
    # to return 5th smallest element: input should be 4
    k_th_smallest_element = 5
    index_of_k_th_smallest_element = k_th_smallest_element - 1
    print(quick_select(lst, 0, len(lst)-1, index_of_k_th_smallest_element))
    
    import random
    import time
    # list of size 1000 incliude integers from 1 to 1e6
    lst= random.sample(range(1, int(1e7)), int(1e6))
    k_th_smallest_element = (len(lst)//4) * 3
    index_of_k_th_smallest_element = k_th_smallest_element - 1
    print("time to find kth smallest element using quick_select:")
    t1 = time.time()
    print(quick_select(lst, 0, len(lst)-1, index_of_k_th_smallest_element))
    print(time.time() - t1)
