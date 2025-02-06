# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:05:47 2021

@author: ATA
"""
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
class SinglyLinkedList:
    
    
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
        self.size +=1
    
    
    def iter(self):
        """ to access all data of list for client, make method that returns a generator(SinglyLinkedList.iter() creates iterable object)"""
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val
            
    #delete a note based on data it contain (data provided by client)

    def delete(self,data):
        """ To delete the nodes which contain the specific data provided by user. 
        detele method has O(n)"""
        current = self.tail            
        prev = self.tail    
        while current:
            if current.data == data:
                # reorganize the list of deteling data found at the beginig of list
                if current == self.tail:
                    self.tail = current.next
                #reorganize the list if deleting data found at middle or end of list
                else:
                    prev.next = current.next
                self.size -= 1
                # if you want the delete method remove first accurance only, use return here to get out of method after first occurance
                #return
            prev = current 
            current = current.next
            
    # to clear the list , whcih is done by clearing pointer head adn tail by setting them to none
    def clear(self):
        """clear the entire list"""
        self.tail = None
        self. head = None
        self.size = 0 
    # to print the list    
    def __str__(self):
        r = "["
        current = self.tail
        while current:   
            if current.next :
                r = r + str(current.data) + ", "
                current = current.next   
            else:
                r = r + str(current.data)
                current = current.next
        r = r + "]"
        return r    

s = SinglyLinkedList()
s.append(0)
s.append(5)
s.append(8)
for item in s:
    print(item)    