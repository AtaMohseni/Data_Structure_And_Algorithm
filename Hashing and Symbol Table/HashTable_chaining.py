# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:34:41 2022

@author: ATA
"""

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None]*self.size
        self.count = 0
        
        
    def _hash(self,key):
        """ calculate the hash value of a given key. this is internal method"""
        
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size
    
    def put(self, key, value):
        """ method to store key/value in hash table"""
        
        item = HashItem(key, value)
        h = self._hash(key)

        if self.slots[h] is None:
            self.count += 1    
            self.slots[h] = [item]
        else:
            for element in self.slots[h]:
                if element.key == key:
                    element.value = value
                    return
            self.slots[h].append(item)
            self.count += 1  
    def __setitem__(self, key, value):
        """ use bult in python method to assign value using bracket, 
        i.e. hashtable[key] = value"""
        
        self.put(key,value)
        
    def get(self, key):
        """ to get and return the value of a given key"""
        
        h = self._hash(key)
        if self.slots[h] is not None:
            for element in self.slots[h]:
                if element.key == key:
                    return element.value
        return None
        
    def __getitem__(self, key):
        """ use bult in python method to return value using bracket,
        i.e, print(hashtable[key])"""
        
        return self.get(key)
    
    def items(self):
        for item in self.slots:
            if item is not None:
                for element in item:
                    yield element.key, element.value
                    
    def __contains__(self,data):
        h = self._hash(data)
        if self.slots[h] is not None:
            for element in self.slots[h]:
                if element.key == data:
                    return True
        return False       
#        for element in self.items():
#            if element[0] == data:
#                return True
                  
    def __str__(self):
        lst =[]
        for element in self.items():
            lst.append(element)
        return str(lst)
    
    
if __name__ == "__main__": 
        
    d_items = [("GOOG",2200),("FB", 320),("TSLA", 600), ("AMZN",3300), ("NVDA",650),("LCID",25)]
    ht = HashTable()
    for symbol,price in d_items:
        ht[symbol] = price
    
    for item in d_items:
        print(item[0])
        print (ht[item[0]])
        
    for element in ht.items():
        print (element)    
    
    print ("AMD" in ht)
    print(ht)