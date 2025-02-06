# -*- coding: utf-8 -*-
"""
Created on Sat May 22 21:24:42 2021

@author: ATA
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None
        
class Tree:
    def __init__(self):
        self.root_node = None
        
     
    def find_min(self):
        """ Complexity of O(h) where h is height of tree"""
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current
    
    
    def find_max(self):
        """ Complexity of O(h) where h is height of tree"""
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current
    
    def insert(self,data):
        """ Complexity of O(h) where h is height of tree"""
        node = Node(data)
        
        if self.root_node == None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    
                    if current == None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current == None:
                        parent.right_child = node
                        return
        
    def breadth_first_traversal(self):
        from collections import deque
        list_of_nodes = []
        traversal_queue = deque([self.root_node])
    
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)
            
            if node.left_child:
                traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)
         
        return list_of_nodes  
    
    def get_node_with_parent(self, data):
        """ To find and return the node and its parent, to be used in remove method"""
        
        parent = None
        current = self.root_node
        if current == None:
            return(parent,None)
        while True:
            if current.data == data:
                return(parent,current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return (parent,current)     
    
    def remove(self,data):
        """ remove the node and replace its position with other appropriate node"""
        """ Complexity of O(h) where h is height of tree"""
        parent, node = self.get_node_with_parent(data)
        if parent == None and node == None:
            return False
        
        #get the children count for removing node
        children_count = 0
         
        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child == None) and (node.right_child == None):
            children_count = 0
        else:
            children_count = 1
     
        #remove node based on its children counts:
        
        #case which removing node has 0 child    
        if children_count == 0:
            if parent:
                if parent.right_child == node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None
                
        # case which removing node has 1 child
        elif children_count ==  1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child
                
            if parent:
                if parent.left_child == node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
                    
            else:
                self.root_node = next_node
                
        # case which removing node has 2 child    
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            # remove and replace new node into deleting node positiion
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
                
            node.data = leftmost_node.data
            
            #re order the new node dependencies
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child
    
    
    
    
    
if __name__ == "__main__":    
    
    t = Tree()                   
    t.insert(10)
    t.insert(6)
    t.insert(12)
    t.insert(9)
    t.insert(3)
    t.insert(1)
    t.insert(5)
    t.insert(4)
    
    #print(t.find_min().data)
    #print(t.find_max().data)
    print(t.breadth_first_traversal())
    t.remove(3)
    print(t.breadth_first_traversal())