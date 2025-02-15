# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:13:23 2021

@author: ATA
"""

def BubbleSort(unordered_list):
    """ worst case complexity O(n^2), best case O(n) input list is alredy ordered"""
    iteration_number = len(unordered_list) - 1
    for i in range(iteration_number):
        for j in range(iteration_number):
            if unordered_list[j] > unordered_list[j+1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j+1]
                unordered_list[j+1] = temp
    return unordered_list



def InsertionSort(unsorted_list):
    """ worst case complexity O(n^2), best case O(n) input list is alredy ordered"""
    for index in range(1, len(unsorted_list)):
        search_index = index
        insert_value = unsorted_list[index]
        
        while search_index > 0 and unsorted_list[search_index - 1] > insert_value:
            unsorted_list[search_index] = unsorted_list[search_index - 1]
            search_index -= 1
        unsorted_list[search_index] = insert_value
        
    return unsorted_list




def selection_sort(unsorted_list):
    """ worst case complexity O(n^2)"""
    size_of_list = len(unsorted_list)
    
    for i in range(size_of_list):
        for j in range(i+1,size_of_list):
            
            if unsorted_list[j] < unsorted_list[j]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = temp
                
    return unsorted_list

########################### 
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

def quick_sort(unsorted_array,first,last):
    """worst case O(n^2), average and best case O(n log n)"""
    """because of the prtition funcction, entire sorting improve compare to other method """
    """ to furture impove the performance, chose pivot point as median of list instead of
    first element in list, which improve the worst case to be O(n log n). 
    To find median, refer to deterministic section algoritm method in chapter 11 and
    fin median_of_medians function"""
    
    if last - first <=0:
        return
    else:
        partition_point = partition(unsorted_array, first, last)
        quick_sort(unsorted_array, first, partition_point - 1)
        quick_sort(unsorted_array, partition_point + 1, last)
    return unsorted_array

if __name__ == "__main__":  
    
    lst = [45,23,87,12,32,4]
    print(BubbleSort(lst))
    print(InsertionSort(lst))
    print(selection_sort(lst))
    print(quick_sort(lst,0,len(lst)-1))