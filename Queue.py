#--------------- QUEUE DATA STRUCTURE -----------------------

# Queue is a data structure where you can add elements to the end of the queue and then remove elements from the beginning.
# Queue follows the principle of First In First Out(FIFO) which means element which is added first will be accessed first.
# It's like a queue of people where people standing first in the queue will be processed first
# Common use case of Stack is like customer care hotline, banking txns, printer queues etc
# Both ENQUEUE and DEQUEUE in a queue operate at different ends of the queue

#--------- Common Operations involving STACK --------------

# Q.enqueue(e): Add element e to the back of queue Q.
# Q.dequeue( ): Remove and return the first element from queue Q;an error occurs if the queue is empty.
# Q.first/peek(): Return a reference of the front element of Queue Q, without removing it; an error occurs if the queue is empty.
# Q.is_empty( ): Return True if Q does not contain any elements.
# Q.is_full(): Return true if Q is full
# len(Q): Return the number of elements in Queue Q

# All above operations have time complexity of O(1) and space complexity of O(n) since we need n space in memory to hols queue of n length
#** There are 2 ways to implement queue in python, first one is custom method like as shown below and other one is by using **PYTHON INBUILT QUEUE CLASS**

# ----------Custom implementation in Python -----------------

class MyQueue:
    
    def __init__(self):
        
        """ Create a new queue."""
        
        self.items = []

    def is_empty(self):
        
        """ Returns true if queue is empty """  
    
        return len(self.items) == 0

    def enqueue(self, item):
        
        """ Add a new element to the end of queue."""
        
        self.items.append(item)

    def dequeue(self):
        
        """ Remove a element from the beginning of queue."""
        
        return self.items.pop(0)

    def size(self):
        
        """ Returns the size of the queue."""
        
        return len(self.items)
    
    def peek(self):
        
        """ Have a look at first element of the queue."""
        
        if self.is_empty():
            raise Exception("Nothing to peek")
       
        return self.items[0]

queue1 = MyQueue()
queue1.enqueue(20)
queue1.enqueue(30)
print(queue1.items)
queue1.dequeue()
print(queue1.items)

# ----------Using inbuilt python class for queue -----------------

from queue import Queue

q = Queue() #creating an instance of a builtin class Queue
q.put(20)  # put() method is similar to enqueue method which adds element at the end and returns None
q.put(40)
q.put(30)
print(q.qsize())   #print the size of q
print(q.get()) # get() method is similar to dequeue method which removes element from the front and returns the number
print(q.get())
print(q.full()) #Checks if q is full
print(q.empty()) #Checks if q is empty

