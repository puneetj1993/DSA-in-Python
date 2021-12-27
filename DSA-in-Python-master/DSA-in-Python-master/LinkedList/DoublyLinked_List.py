#--------------- Doubly Linked List DATA STRUCTURE -----------------------

# Linked list in which each node keeps an explicit reference to the node before it and a reference to the node after it.
# Such a structure is known as a doubly linked list
# In a singly linked list, each node maintains a reference to the node that is immediately after it.
# Linked list has some limitations-
   # -we are unable to efficiently delete a node at the tail of the list.
   # -we cannot efficiently delete an arbitrary node from an interior position of the list if only given a reference to that node, because
    # we cannot determine the node that immediately precedes the node to be deleted
# Doubly linked list provides the greater symmetry than linked lists
# We have the dummy Head and Tail nodes in doubly linked list
# These “dummy” nodes are known as sentinels (or guards), and they do not store elements of the primary sequence
# We have circular linked list as well where Tail instead of pointing to the None points back to the head of the linked list(no implementation)


# ----------Custom implementation in Python -----------------

# Class representing a node
class Node:
    def __init__(self,data,prev,next):
        self.data = data
        self.prev = prev
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

# Class representing a doublt linked List. 
class DoublyLinkedList:

    def __init__(self):
        self.header = None      # Sentinel Header node
        self.trailer = None     # Sentinel Trailer node
        self.header.next = self.trailer     #Trailer is after header
        self.trailer.prev = self.header     #header is before trailer
        self.size= 0                        #no of elements


    def add(self,data,predecessor,successor):
        
        node1 = Node(data,predecessor,successor)
        predecessor.next = node1
        successor.prev = node1
        self.size+=1

    def __len__(self):
       
        return self.size

    def isEmpty(self):
        
        return self.size == 0

    
    def delete node(self, node):
    
     
        predecessor = node. prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size −= 1
        element = node.element      # record deleted element
        node.prev = node.next = node.element = None        # deprecate node
        return element      # return deleted element
#Here we can see that adding and deleting is very easy. we just need to change successor.next and predecessor.prev and its done
    

