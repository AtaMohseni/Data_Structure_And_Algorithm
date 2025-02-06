# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:45:11 2022

@author: ATA
"""
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
        
from random import randint
class Tracks:
    def __init__(self,title = None):
        self.title = title
        self.length = randint(5,10)
        
        
import time
class MediaPlayerQueue(NodeQueue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        new_track = Tracks(track)
        self.enqueue(new_track)  
    def play(self):
        
        while self.count > 0:
            current_track_node = self.dequeue()
            print("now playing {}".format(current_track_node.title))
            time.sleep(current_track_node.length)
            
if __name__ == "__main__":
    
    MediaPlayer = MediaPlayerQueue()                
    MediaPlayer.add_track("white whistler") 
    MediaPlayer.add_track("better butter") 
    MediaPlayer.play()
           