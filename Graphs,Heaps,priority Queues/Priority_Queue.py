# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:40:16 2022

@author: ATA
"""
    
class PriorityQueue:
    """ this is implementation of Max Heap, So item with highest priority is 
    at the root of the heap. Items are added to the heap list as a tuple of
    (pritority value, item)"""
    
    def __init__(self):
        self.heap = [0] # list of tuples (priority value, item) start taking position from index 1 of list
        self.size = 0      # self.size will be less than length of self.minheap  by 1, to remind us we started adding nodes from index 1
        
    def arrange(self, k):
        
        while k // 2 > 0:  # untill we check the root node position which k = 1, k//2 = 0
            
            if self.heap[k][0] > self.heap[k//2][0]:  # compare the value of index k to its parent
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
        
        elif self.heap[k*2][0] > self.heap[k*2+1][0]:
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
            
            if self.heap[k][0] < self.heap[ma][0]:  # swap with max child as needed
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
            sorted_list.append(n[1])
        return sorted_list    

if __name__ == "__main__":
    
    data = [(1,"coffee"),(2,"vanilla icecream"),(6,"burger"),(10,"nugget"),(1,"decaff coffee"),(2,"chocolate icecream"),(12,"chicken") ]  
    PQ = PriorityQueue()
    for i in data:
        PQ.insert(i)
    
    print ("\nsorted data base on priorities:",PQ.heap_sort())    