# -*- coding: utf-8 -*-
"""
Created on Thu May 20 19:40:04 2021

@author: ATA
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        
        if self.top:
            node.next =self.top  
            self.top = node
        else:
            self.top = node
        self.size +=1
        
        
    def pop(self):
        
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None
        
    def peek(self):
        
        if self.top:
            return self.top.data
        else:
            return None
                
        
############
""" example to use stack"""

def check_bracket(statement):
    """ this function check if number of opening bracket is as same as closing brackets
    also, it make sure each bracket is inside and other bracket"""

    stack  = Stack()   
    for ch in statement:
        if ch in ("{","[","("):
            stack.push(ch)
        if ch in ("}","]",")"):
            last = stack.pop()
            if last == "{" and ch == "}":
                continue
            elif last == "[" and ch == "]":
                continue
            elif last == "(" and ch == ")":
                continue
            else:
                return False
    if stack.size > 0:
        return False
    else:
        return True 

if __name__ == "__main__":    
    
    s = "{(aa)(bb)}[hsello](((this)is)a)test}"    
    print(check_bracket(s))
    
    s = "{(aa)(bb)}[hsello](((this)is)a)((test"
    print(check_bracket(s))