# -*- coding: utf-8 -*-
"""
Created on Thu May 27 19:32:32 2021

@author: ATA
"""

class MinHeap:
    def __init__(self):
        self.heap = [0]  # heap value start taking position from index 1 of list
        self.size = 0       # self.size will be less than length of self.minheap  by 1, to remind us we started adding nodes from index 1
        
    def arrange(self, k):
        """ To re-arrange the heap after adding new node """
        while k // 2 > 0:  # untill we check the root node position which k = 1, k//2 = 0
            
            if self.heap[k] < self.heap[k//2]:  # compare the value of index k to its parent
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
                
            k = k //2 # move up to the tree toward node
            
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)
    
    def minindex(self, k):
        """ to make code look clearner, it compare both children of parent (parent is in indext k)
        and retrun the index of smaller child."""
        
        if k * 2 + 1 > self.size: # case which parent at index k has only 1 child which ofcourse is in left side
            return k *2
        
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k * 2
        else:
            return k * 2 + 1
    
    def sink(self, k): 
        """to be used in pop() method to sink down the node at index k to its appropriate position.
        since pop method remove and return root node, the last element of heap list
        will take position of root node, it then start sinking down from root node (k=1) to its
        appropriate location"""
        
        while k*2 <= self.size:  #loop till we reach end of heap
            mi = self.minindex(k) # optain the index of minimum child
            
            if self.heap[k] > self.heap[mi]:  # swap with min child as needed
                self.heap[k],self.heap[mi] = self.heap[mi],self.heap[k]
            
            k = mi # make sure we are moving down to tree
            
    def pop(self):
        """ Method to remove and return root node (which is minimum node of min-heap)"""
        item = self.heap[1]  # pop method only will be used to remove and return root node
        self.heap[1] = self.heap[self.size] # the last item of heam took position as root node
        self.size -= 1
        self.heap.pop()  #here pop() is a list method to remove the last item if self.heap list
        self.sink(1)
        return (item)
    
    def heap_sort(self):
        sorted_list = []
        for node in range(self.size):
            n = self.pop()
            sorted_list.append(n)
        return sorted_list

class MaxHeap:
    def __init__(self):
        self.heap = [0] # heap value start taking position from index 1 of list
        self.size = 0      # self.size will be less than length of self.minheap  by 1, to remind us we started adding nodes from index 1
        
    def arrange(self, k):
        
        while k // 2 > 0:  # untill we check the root node position which k = 1, k//2 = 0
            
            if self.heap[k] > self.heap[k//2]:  # compare the value of index k to its parent
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k] #swap the child and parent position
                
            k = k //2 # move up to the tree toward node 
            
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)      
        
    def maxindex(self, k):
        """ to make code look clearner, it compare both children of a parent (parent is in indext k)
        and retrun the index of larger child."""
        
        if k * 2 + 1 > self.size: # case which parent at index k has only 1 child which ofcourse is in left side
            return k *2
        
        elif self.heap[k*2] > self.heap[k*2+1]:
            return k * 2
        else:
            return k * 2 + 1
        
    def sink(self, k):
        """to be used in pop() method to sink down the node at index k to its appropriate position.
        since pop method remove and return root node, the last element of heap list
        will take position of root node, it then start sinking down from root node (k=1) to its
        appropriate location"""

        while k*2 <= self.size:  #loop till we reach end of heap
            ma = self.maxindex(k) # optain the index of larger max child
            
            if self.heap[k] < self.heap[ma]:  # swap with max child as needed
                self.heap[k],self.heap[ma] = self.heap[ma],self.heap[k]
            
            k = ma # make sure we are moving down to tree
            
    def pop(self):
        """ Method to remove and return root node (which is maximum node of max-heap)"""
        item = self.heap[1]  # pop method only will be used to remove and return root node
        self.heap[1] = self.heap[self.size] # the last item of heam took position as root node
        self.size -= 1
        self.heap.pop()  #here pop() is a list method to remove the last item if self.heap list
        self.sink(1)
        return (item) 
    
    def heap_sort(self):
        sorted_list = []
        for node in range(self.size):
            n = self.pop()
            sorted_list.append(n)
        return sorted_list
    
if __name__ == "__main__":    
        
    # testing the heap
    
    data = [4,8,7,2,9,10,5,1,3,6,77,25,66,33,19,-5]
    hmin = MinHeap()
    hmax = MaxHeap()
    
    for i in data:
        hmin.insert(i)
        hmax.insert(i)
        
    print(hmin.heap)
    print(hmax.heap)
       
    print ("\nsorted data from min:",hmin.heap_sort())
    print ("sorted data from max:",hmax.heap_sort())
    ###################################### Python Built in Min Heap #################
    
    ####### Min Heap
    import heapq
    heapWithValues = [3,1,2]
    heapq.heapify(heapWithValues)
    print(heapWithValues)
    heapq.heappush(heapWithValues, 5)
    print(heapWithValues)
    
    # remove the root element
    heapq.heappop(heapWithValues)
    print(heapWithValues)
    ##################### Max Heap
    import heapq
    heapWithValues = [3,2,3,1,2,4,5,5,6]
    k = 4
    maxheap = [-x for x in heapWithValues]
    
    heapq.heappush(maxheap, -1*15)
    
    i = 0
    while i < k:
        item = heapq.heappop(maxheap)
        i += 1
    print(-1*item)