# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:06:07 2021

@author: ATA
"""
from collections import deque

def breadth_first_search(graph,root):
    """ Input is a graph dictionary which keys are nodes and values are adjacent vertices
    to that node. root node can be choose randomly"""
    """ O(|V| + |E|)"""
    visited_vertices = []
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root
    
    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adj_nodes = graph[node]
        # pick the element in adj_nodes which is not in visited_vertices. remaning_elements is a set
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)
        
    return visited_vertices


if __name__ == "__main__": 
    
    graph = dict()
    graph["A"] = ["B","G","D"]
    graph["B"] = ["A","F","E"]
    graph["C"] = ["F","H"]
    graph["D"] = ["F","A"]
    graph["E"] = ["B","G"]
    graph["F"] = ["B","D","C"]
    graph["G"] = ["A","E"]
    graph["H"] = ["C"]
    
    print(breadth_first_search(graph,"A"))