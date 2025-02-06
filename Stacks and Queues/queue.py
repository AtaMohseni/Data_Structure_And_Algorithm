# -*- coding: utf-8 -*-
"""
Created on Thu May 20 22:21:15 2021

@author: ATA
"""

class ListQueue:
    """Implementation of List-based Queues, enqueue method is ineficient for 
    large lists because every time it needs to shift all data to the right""" 
    def __init__(self):
        self.items = []
        self.size = 0
        
    def enqueue(self,data):
        self.items.insert(0,data)
        self.size += 1
    def dequeue(self):
        data = self.item.pop()
        self.size -= 1
        return data
    
##############################################
class StackQueue:
    """Implementation of List-based Queues, dequeue method has O(n)"""
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack =[]
        self.inbount_size = 0
        self.outbound_size = 0
    def enqueue(self, data):
        self.inbound_stack.append(data)
        self.inbount_size +=1
        
    def dequeue(self):
        # check if outbount stack is empty(it has available room)
        if not self.outbound_stack:
            # put all elements of inbound stack to outbount stack, O(n)
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
                self.outbound_size += 1
                self.inbound_size -= 1
        self.outbound_size -=1
        return self.outbound_stack.pop()
############################################## 

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next =None
        self.prev = None
    
    
class NodeQueue:
    """here self.tail refers to the end of the list and self.head refers to 
    beginign of the list (which is contrary to the singly linked list class that
    we created in other file)"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def enqueue(self, data):
        new_node = Node(data)
        if self.head ==None:
            self.head = new_node
            self.tail = self.head
            
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node            
            
        
        self.count +=1
        
    def dequeue(self):
        
        if self.count == 0:
            return
        elif self.count == 1 :
            remove = self.head
            self.head = None
            self.tail = None
            self.count -= 1
            return remove.data
        else:
            remove = self.head
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            return remove.data

    