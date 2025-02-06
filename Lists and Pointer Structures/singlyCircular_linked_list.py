# -*- coding: utf-8 -*-
"""
Created on Thu May 20 12:41:47 2021

@author: ATA
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
class SinglyCircularLinkedList:
    
    
    def __init__(self):
        
        self.tail = None # variable points to the first node in list
        self.head = None # variable points to the last node in the list
        self.size = 0
    
    def append(self,data):
        """ to append new node at the end of lis.the point which we append new
        node is self.head, and self.tail points to the first node in the list"""
        node = Node(data)
        
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.head.next = self.tail    
        self.size +=1
    
    
    def iter(self):
        """ to access all data of list for client, make method that returns a generator(SinglyLinkedList.iter() creates iterable object)"""
        # note that the while loop condition is different from singlylinkedlist bc current is not gonna be None anymore
        current = self.tail
        prev = self.tail
        while self.size > 0 and (prev == current or prev != self.head):
            if self.size == 1:
                val =current.data
                yield val
                break
            else:    
                val = current.data
                prev = current 
                current = current.next
                yield val
            
    #delete a note based on data it contain (data provided by client)

    def delete(self,data):
        """ To delete first ooccurance of nodes which contain the specific data provided by user. 
        detele method has O(n)"""
        current = self.tail            
        prev = self.tail
        # note that the while loop condition is different from singlylinkedlist bc current is not gonna be None anymore
        while self.size > 0 and (prev == current or prev != self.head):
            if current.data == data:
                # if deletinf data found in list of size 1
                if self.size == 1 :
                    self.tail = None
                    self.head = None
                # if deteling data found at the beginig of list of size larger than 1
                elif current == self.tail:
                    self.tail = current.next
                    self.head.next = self.tail
                #if if deleting data found at middle or end of list of size larger than 1
                else:    
                    prev.next = current.next
                self.size -= 1
                # if you want the delete method remove first accurance only, use return here to get out of method after first occurance
                return
            prev = current 
            current = current.next
    
    def clear(self):
        """clear the entire list"""
        self.tail = None
        self. head = None
        self.size =0
    # to print the list    
    def __str__(self):
        r = "["
        current = self.tail
        prev = self.tail
        # note that the while loop condition is different from singlylinkedlist bc current is not gonna be None anymore
        while self.size > 0 and (prev == current or prev != self.head):
            if self.size == 1:
                r = r + str(current.data)
                break
            elif current != self.head :
                r = r + str(current.data) + ", "
            else:
                r = r + str(current.data)
            prev = current    
            current = current.next
        r = r + "]"
        return r   