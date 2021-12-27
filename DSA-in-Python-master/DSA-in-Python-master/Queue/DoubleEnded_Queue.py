#--------------- Double Ended QUEUE DATA STRUCTURE -----------------------

# Double ended queue/deck/deque is a data structure that supports insertion and deletion at both the front and the back of the queue
# It's like a queue of people waiting at the restraunt where people standing first in the queue will be processed first and if the last people wants to leave because of waitng time
# Then he can leave from the end as well


#--------- Common Operations involving STACK --------------

# D.add_first(e): Add element e to the front of deque D.
# D.add_last(e): Add element e to the back of deque D.
# D.delete_first( ): Remove and return the first element from deque D;an error occurs if the deque is empty.
# D.delete_last( ): Remove and return the last element from deque D;an error occurs if the deque is empty.
# D.first(): Return (but do not remove) the first element of deque D;an error occurs if the deque is empty.
# D.last(): Return (but do not remove) the last element of deque D;an error occurs if the deque is empty.
# D.is_empty( ): Return True if deque D does not contain any elements.
# len(D): Return the number of elements in deque D;

# All above operations have time complexity of O(1) and space complexity of O(n) since we need n space in memory to hols queue of n length
# Deque can be implemented by using pyhton inbuild class from collections.deque module as shown below-

## Our Deque           collections.deque methods   Description
##
## len(D)              len(D)                      number of elements
## D.add_first( )      D.appendleft( )             add to beginning
## D.add_last( )       D.append()                  add to end
## D.delete_first( )   D.popleft( )                remove from beginning
## D.delete_last( )    D.pop()                     remove from end
## D.first()           D[0]                        access first element
## D.last( )           D[−1]                       access last element
##                     D[j]                        access arbitrary entry by index
##                     D[j] = val                  modify arbitrary entry by index
##                     D.clear( )                  clear all contents
##                     D.rotate(k)                 circularly shift rightward k steps
##                     D.remove(e)                 remove first matching element
##                     D.count(e)                  count number of matches for e

# ----------Custom implementation in Python -----------------

class DeQueue:
    
    def __init__(self):
        
        """ Create a new queue."""
        
        self.items = []

    def is_empty(self):
        
        """ Returns true if queue is empty """  
    
        return len(self.items) == 0

    def add_first(self, item):
        
        """ Add a new element at the front of queue."""
        
        self.items.insert(0,item)

    def add_last(self, item):
        
        """ Add a new element to the end of queue."""
        
        self.items.append(item)

    def delete_first(self):
        
        """ Remove a element from the beginning of queue."""
        
        return self.items.pop(0)
    
    def delete_last(self):
        
        """ Remove a element from the beginning of queue."""
        
        return self.items.pop()


    def size(self):
        
        """ Returns the size of the queue."""
        
        return len(self.items)
    
    def first(self):
        
        """ Have a look at first element of the queue."""
        
        if self.is_empty():
            raise Exception("Nothing to peek")
       
        return self.items[0]
       
    def last(self):
        
        """ Have a look at first element of the queue."""
        
        if self.is_empty():
            raise Exception("Nothing to peek")
       
        return self.items[-1]

q1 = DeQueue()
q1.add_first(20)
q1.add_first(30)
print(q1.items)
q1.delete_last()
print(q1.items)


