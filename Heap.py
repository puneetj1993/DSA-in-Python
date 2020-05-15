#---------- BINARY HEAP DATA STRUCTURE -------------

# A HEAP is a binary tree data structure but with 2 properties-
# First one is, binary tree should be a complete binary tree. A heap T with height h is a complete binary tree if levels 0,1,2, . . . ,h−1 of T have the maximum number of nodes possible
# and the remaining nodes at level h reside in the leftmost possible positions at that level.
# Second one is,Root element should be the min/max depending on the type of HEAP. That means, child should be greater/smaller than their parents

#----------Types of HEAP----------------
# MAX HEAP - ROOT element is the largest element of the tree and parents should be greater than children themselves so, leaf nodes are the smallest.
# MIN HEAP - ROOT element is the smallest element of the tree and parents should be smaller than children themselves so, leaf nodes are the largest.

# If we are not following the above 2 properties then our Binary tree is not a heap tree. So, to make a tree as HEAP then first it should be complete tree and then root should be smallest/largest depending on the type of head.

#-------Different operations in HEAP----------

# INSERTION OF AN ELEMENT - Please below steps to insert any element in the HEAP-
# 1. Insert an element in such a way that if will be complete tree after inserting a node.So, we will usually enter this node at the leftmost position if all the elements at the previous level are filled
#    and if there is a space for new element in the previous level than fill it from the left position irrespective of whether this new node is smaller/larger than parent.
# 2. Now, complete binary tree property is checked and swap the inserted elements in such a way that it follows the other required property that root/parents hsould be larger/smaller than children.Eg:
# 3. Suppose we are adding elements in a MAX HEAP and we have inserted that at the lefmost position then we have to compare this element with its parent and so on. If this element > parent then swap it.
#    In this way swap the element with its parent depending on the condition that element>parent and your root should be maximum(MAX HEAP).
# So, total swaps needed = height of tree which is O(logN) hence COMPLEXITY OF INSERTION is O(LogN) and the direction of swapping the elements is UPWARD (leaf -> Root)

# DELETION OF AN ELEMENT - Please follow the below steps
# 1. IN HEAP, element is ONLY ALLOWED TO BE DELETED FROM ROOT. we can't remove element from any other position,
# 2. After ROOT element is deleted, compare its child nodes and then swap the largest one to root(in case of MAX HEAP) and then compare the empty node's child and repeat it till you get the HEAP.

# So, total swaps needed = height of tree which is O(logN) hence COMPLEXITY OF DELETION is also O(LogN) and the direction of swapping the elements is DOWNWARDS( Root -> leaf)

#------------ HEAP SORT -----------------------------
# During deletion we noticed that root element which is largest (in case of MAX HEAP) is getting deleted first. So, if we delete all the root elements by followin this approach and storing them in an array
# then we are getting a sorted array (Max elemnt -> 2nd amx -> 3rd max and so on) THIS TYPE OF SORTING IS CALLED HEAP SORT with COMPLEXITY of O(NLogN) as we have to delete n element and complexity of 1 element is logN sp n*LogN

#Heap can also be represented in array form like BST like root->left to right nodes at each level in the list starting form 0 index

#--- Application of HEAP DATA STRUCTURE---------

# HEAP is mainly used to implement PRIORITY QUEUES data structure.

#---------------- Python3 implementation of Max Heap ---------------------------
  
import sys 
  
class MaxHeap: 
  
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = sys.maxsize 
        self.FRONT = 1
  
    # Function to return the position of 
    # parent for the node currently 
    # at pos 
    def parent(self, pos): 
        return pos//2
  
    # Function to return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self, pos): 
        return 2 * pos 
  
    # Function to return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self, pos): 
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False
  
    # Function to swap two nodes of the heap 
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    # Function to heapify the node at pos 
    def maxHeapify(self, pos): 
  
        # If the node is a non-leaf node and smaller 
        # than any of its child 
        if not self.isLeaf(pos): 
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                self.Heap[pos] < self.Heap[self.rightChild(pos)]): 
  
                # Swap with the left child and heapify 
                # the left child 
                if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.maxHeapify(self.leftChild(pos)) 
  
                # Swap with the right child and heapify 
                # the right child 
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.maxHeapify(self.rightChild(pos)) 
  
    # Function to insert a node into the heap 
    def insert(self, element): 
        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] > self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+str(self.Heap[i])+" LEFT CHILD : "+ 
                               str(self.Heap[2 * i])+" RIGHT CHILD : "+
                               str(self.Heap[2 * i + 1])) 
  
    # Function to remove and return the maximum 
    # element from the heap 
    def extractMax(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.maxHeapify(self.FRONT) 
        return popped 
  
# Driver Code 
if __name__ == "__main__": 
    print('The maxHeap is ') 
    minHeap = MaxHeap(15) 
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
  
    minHeap.Print() 
    print("The Max val is " + str(minHeap.extractMax())) 
