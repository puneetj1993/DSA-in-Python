#--------------- TREE DATA STRUCTURE -----------------------

# Trees are a data structure which represents the heirerical data instead of linear data represented by linked list, stack and queue.
# Here in Trees, we have a base node called as ROOT that has no incoming edges.
# All other nodes coming out of ROOT are CHILDREN of ROOT hence, ROOT is parent and rest other nodes are called as children of ROOT.
# Similarly, any other node can have multiple children and a single parent.
# Nodes which don't have any children, usually th last nodes are called as LEAF NODES
# Nodes having a same parent can be called as SIBLING NODES
# An EDGE connects two nodes to show that there is a relationship between them. Every node (except the root) is connected by exactly one incoming edge from another node.
# Each node may have several outgoing edges.
# A PATH is an ordered list of nodes that are connected by edges.Eg: A -> B -> C -> D -> E
# A SUBTREE is a set of nodes and edges comprised of a parent and all the descendants of that parent. Eg: left subtree and right subtree
# The LEVEL of a node n is the number of edges on the path from the root node to n. Eg: A->B->C. A is at level1, B is at level 2 and C is at level 3
# The HEIGHT of a tree is equal to the maximum level of any node in the tree. Eg: A->B->C->D. Height of this type of tree is 4 as there are 4 levels

#---------------------- BINARY TREE -----------------------------

# If any TREE has atmost 2 children (0,1,2) then this type of tree is called as BINARY TREE.
# In Binary Tree there is a special case of BINARY SEARCH TREE (BST) where all the nodes with data<parent node are part of left subtree and data>parent node are part of right subtree starting from ROOT.
# BST are the mostly used trees hence, we will study only BST

#------------------------ Common Operations on the BST --------------------------------------

# INSERTION of a node in a BST: There is exactly one location into which an elements could be inserted. As mentioned above, if this new node is less than root node then it will go to the left and vice versa.
# Complexity of inserting a node in BST is  O(logN) to the base 2.

# SEARCHING for a node is also O(logN) for a balanced tree
# MINIMUM VALUE stored in a tree: Value of the left-most node of the tree is the minimum.
# MAXIMUM VALUE stored in a tree: Value of right-most node of the tree is the maximum
# MAXMUM DEPTH: depth of a particular node in a binary search tree, what we mean is its distance from the root and Max depth of the tree is the maximum distance between the root node and any of its leaf nodes
# SUM PATH: There is any path from the root to a leaf node within the binary search tree where the sum of all the values in the nodes along that path sum up to the given number.
# Eg: A->B->C->D here if A+B+C+D = some given no this is a sum path
# Height of complete BST is logN

#---------- Traversal in BST -----------------
# There are 2 kind of traversals Breadth first and Depth First traversals
# In BREADTH FIRST TRAVERSAL, the order of traversal is root -> left nodes at a level -> right nodes at the same level ->left nodes at the enxt level ->continue...It is similar to moving from left to right
# There are 3 types of DEPTH FIRST TRAVERSALS
# In PRE ORDER TRAVERSAL, Root ->Left subtree -> Right subtree (Consider each node as root and then print itself first and then its left and then its right)
# In IN ORDER TRAVERSAL, Left -> Root -> Right (Consider each node as root and then print its left childs first and then node itself and then its right)
# In POST ORDER TRAVERSAL, Left -> Right -> Root (Consider each node as root and then print its left first and then its right childs and then node itself)

# ----------Custom implementation in Python -----------------

class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val
        self.size = 0

def insert(root, node):
    if root is None:
        root = node
    else:
        if node.data<=root.data:
            if root.l_child is None:
                root.l_child = node
            else:
                insert(root.l_child, node)
        elif node.data > root.data:
            if root.r_child is None:
                root.r_child = node
            else:
                insert(root.r_child, node)
    root.size+= 1
def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)
    
def post_order_print(root):
    if not root:
        return        
    post_order_print(root.l_child)
    post_order_print(root.r_child)
    print(root.data)

r = Node(57)
A=insert(r,Node(27))
B = insert(r,Node(60))
C=insert(r,Node(37))
print(r.size)


