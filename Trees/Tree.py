# -*- coding: utf-8 -*-
"""
Created on Sat May 22 11:02:42 2021

@author: ATA
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None
        

########################################Depth first search traversal
def depth_search_inorder_traversal(root_node):
    current = root_node
    if current is None:
        return
    depth_search_inorder_traversal(current.left_child)
    print(current.data)
    depth_search_inorder_traversal(current.right_child)
    

def depth_search_preorder_traversal(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    depth_search_preorder_traversal(current.left_child)
    depth_search_preorder_traversal(current.right_child)

def depth_search_postorder_traversal(root_node):
    current = root_node
    if current is None:
        return
    depth_search_postorder_traversal(current.left_child)
    depth_search_postorder_traversal(current.right_child)
    print(current.data)
    
################################################### Breadth First Search traversal
from collections import deque

def breadth_first_traversal(root_node):
        list_of_nodes = []
        traversal_queue = deque([root_node])
    
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)
            
            if node.left_child:
                traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)
         
        return list_of_nodes    

if __name__ == "__main__":
    
    n1 = Node("root Node")
    n2 = Node("left child")
    n3 = Node("right child")
    n4 = Node("left-left grand child")
    n5 = Node("left-right grand child")
    n1.left_child = n2
    n1.right_child = n3
    n2.left_child = n4
    n2.right_child = n5   
    
    print ("\norder of visit In-order search: ")
    depth_search_inorder_traversal(n1)    
    print ("\norder of visit Pre-order search: ")      
    depth_search_preorder_traversal(n1)
    print ("\norder of visit Post-order search: ")      
    depth_search_postorder_traversal(n1)
     
    print("\nBreadth depth traversal:")
    print(breadth_first_traversal(n1))

