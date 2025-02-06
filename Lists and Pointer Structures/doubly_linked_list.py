# -*- coding: utf-8 -*-
"""
Created on Wed May 19 18:45:00 2021

@author: ATA
"""

class Node:
    
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None
 
class DoublyLinkedList(object):
    """here self.head refers to the end of the list and self.tail refers to 
    beginign of the list (which is contrary to the singly linked list class that
    we created in other file)"""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def append(self, data):
        """ append an item to the end of list has O(1)"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # assigning next and prev attributes of the new node, and previously last node 
            new_node.prev = self.tail
            self.tail.next = new_node
            #updating the tail and count
            self.tail = new_node
        self.count += 1
            
    def delete(self, data):
        """ To detele the first occurance of data from the list, O(n)""" 
        
        """ if you want to detelte all accurances, just remove the 
        "return" words everywhereinside delete method """
        current = self.head
        # empty list
        if current is None:
            return
        # delete item if occures at the begining of the list    
        elif current.data == data:    
            self.head = current.next
            self.head.prev = None
            self.count -= 1
            return
        #  delete item occures at the endo of the list. Book is not currect here
        # if item occures several time, with this book approach it deletes the last occurance only
        
        #elif self.tail.data == data:
        #   self.tail = self.tail.prev
        #   self.tail.next = None
        #   node_deleted = True
        
        # traverse trought the list if item occures at the middle or end list
        else:
            while current:
                if current.data == data:
                    #if data occured at the end of list
                    if current.next == None:
                        self.tail = current.prev
                        current.prev.next = None
                    #if data occured at the middle of list    
                    else:
                        current.next.prev = current.prev
                        current.prev.next = current.next
                    
                    self.count -= 1
                    return
                
                current = current.next
        
            
            
    def iter(self):
        """ to access the all data of list for client, make method that returns a generator(SinglyLinkedList.iter() creates iterable object)"""
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val 
    # using __contains__ python special method         
    def __contains__(self, data):
        """ check if item is in the list. O(n)"""
        for node_data in self.iter():
            if node_data == data:
                return True
        return False
    # to print the list
    def __str__(self):
        r = "["
        current = self.head
        while current:   
            if current.next :
                r = r + str(current.data) + ", "
            else:
                r = r + str(current.data)
            current = current.next
        r = r + "]"
        return r
        