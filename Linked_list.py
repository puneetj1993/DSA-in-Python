#--------------- Linked List DATA STRUCTURE -----------------------

# Linked List is a data structure that is a chain of nodes .Each node contains a value and a pointer to the next node in the chain..
# The first field contains the data for the node, and the second field represents a pointer to the next node in the linked list. The first node is called HEAD and the last one is TAIL
# The pointer for the TAIL is NULL as there is no node for reference post TAIL node. When the list is empty, the head pointer points to null.
# The way to get to any of the elements in the list is through the HEAD** that means if we want to access any element other than Head then we have to traverse to the element from HEAD.
# We can't directly access middle element and it has to be traversed through HEAD.


#--------- Common Operations involving Linked List --------------

#------Insertion of a new node-----------

# Add new node to the end of a linked list: We need to traverse the list from Head to Tail and then add new element and set previous tail element ponter to this newly add element
# and set it pointer to Null. Complexity is O(n) where n=no of elements in the list
# Add new node to the start of a linked list: Add new element and set Head to this element and add pointer to the old head element. Complexity is O(1)
# Add new element in the middle somewhere b/w Head and Tail: Add new element and set previous pointer to this element and this element's pointer to next element. Complexity is O(N)

#---------Searching for a node-----------

#Searching will always be from Head and hence complexity is O(n)

#------Deletion of a node-----------

# Deleting new node from the end of a linked list: We need to traverse the list from Head to Tail and then delete the Tail element and set previous element pointer to NULL
# and set Tail to previous element. Complexity is O(n) where n=no of elements in the list
# Deleting new node from the start of a linked list: Delete an element and set Head to the next element . Complexity is O(1)
# Deleting new element in the middle somewhere b/w Head and Tail: Delete an element and set previous pointer to the new next element . Complexity is O(N)


# ----------Custom implementation in Python -----------------

# Class representing a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

# Class representing an unordered linked list. Head should be none for a empty linked list
class LinkedList:

    def __init__(self):
        self.head = None


    def add(self,data):
        """
            Adding new node in the begining of the linked list i.e adding node to the left of a node(O(1)) 
            Self.head is the current node( before adding) hence this would become next for this newly added node
            After this, new node becomes the self.head pointer
        """
        node1 = Node(data)
        node1.setNext(self.head)
        self.head = node1

    def size(self):
        """
            Getting the size of a linked list.
            current = self.head; represents the head and counting should be done from head
            count = 0 ; Counter to count the no of nodes
            current.getNext() to move to the next node
        """
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def isEmpty(self):
        """
            Checking if linked list is empty.
            If head is empty , it means list is empty
        """
        return self.head == None

    def search(self,item):
        """
            Searching for a element from Head.
            Current represents the head
         """
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def remove(self,item):
        """
            Removing an element from linked list
            Current represents the Head
            Previous represents the previous node; Initial is none as there is no node before Head
        """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current              # If we don't find item then assigning current node to Previous node and then increment the current to next node
                current = current.getNext()

        if previous == None:                #This is possible only when Head =item so making head to next node as this will be removed
            self.head = current.getNext()
        else:                               # if item is at any other node than head then updating the previous node pointer to current next node as current will be removed
            previous.setNext(current.getNext())
        
node1 =LinkedList()
node1.add(40)
node1.add(50)
node1.add(12)
node1.remove(50)
print(node1.size())
print(node1.search(50))
