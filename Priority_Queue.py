#---------- PRIORITY QUEUES ----------------------------

# PRIORITY QUEUE is a type of queue but here it doesn't follow FIFO principal. In a priority queue the logical order of items inside a queue is determined by their priority.
# The highest priority items are at the front of the queue and the lowest priority items are at the back
# For example, if the movie cinema decides to serve loyal customers first, it will order them by their loyalty (points or number of tickets purchased).
# In such a case, the queue for tickets will no longer be first-come-first-served, but most-loyal-first-served. The customers will be the “items” of this priority queue while the “priority” or “key” willbe their loyalty.
# The MAIN PROPERTY OF PRIORITY QUEUE is the element with the most highest priority is dequeue(removed/served) first.
# Usually the value of the node/element is set as their priority.

# The best data structure to implement PRIORITY QUEUE is HEAP since complexity is O(LogN). If we use list then the Complexity would be O(N)
# So if we are using say MAX HEAP then root is of MAX value/priority and will be deleted/served first. Hence , its good to use HEAP for priority queues not lists.

#-------------Implementation of Priority queue using Pyhton inbuild heapq module-------------
# Note that heapq only has a min heap implementation, but there are ways to use as a max heap (not covered in this article)

import heapq
customers = []
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))
while customers:
     print(heapq.heappop(q))
#Will print names in the order: Riya, Harry, Charles, Stacy.

#-------------Implementation of Priority queue using Python inbuild QUEUE CLASS -------------
# The PriorityQueue uses the same heapq implementation and thus has the same time complexity. However, it is different in two key ways.
# Firstly, it is synchronized, so it supports concurrent processes (you can read more about here). Secondly, it is a class interface instead of the function based interface of heapq .
# Thus, PriorityQueue is the classic OOP style of implementing and using Priority Queues. The same queue class is also used to implement queue data strucures in python


from queue import PriorityQueue
customers = PriorityQueue() #we initialise the PQ class instead of using a function to operate upon a list. 
customers.put((2, "Harry"))
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((4, "Stacy"))
while customers:
     print(customers.get())
#Will print names in the order: Riya, Harry, Charles, Stacy.

# We can also implement our own custom priority queue code.
