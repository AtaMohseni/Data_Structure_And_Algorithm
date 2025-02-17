# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:34:34 2021

@author: ATA
"""

def depth_first_search(graph,root):
    """ Input is a graph dictionary which keys are nodes and values are adjacent vertices
    to that node. root node can be choose randomly"""
    visited_vertices = []
    graph_stack = []
    
    graph_stack.append(root)
    node = root
    
    while len(graph_stack) > 0:
        if node not in visited_vertices:
            visited_vertices.append(node) # note that this node is still remains in stack
        adj_nodes = graph[node] 
        
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                node  = graph_stack[-1]
            continue
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))
            
            first_adj_node = sorted(remaining_elements)[0]
            graph_stack.append(first_adj_node)
            node = first_adj_node
    return visited_vertices


if __name__ == "__main__": 
    
    graph = dict()
    graph["A"] = ["B","S"]
    graph["B"] = ["A"]
    graph["S"] = ["A","G","C"]
    graph["D"] = ["C"]
    graph["G"] = ["S","F","H"]
    graph["H"] = ["G","E"]
    graph["E"] = ["C","H"]
    graph["F"] = ["C","G"]
    graph["C"] = ["D","S","E","F"]
    
    print(depth_first_search(graph,"A"))