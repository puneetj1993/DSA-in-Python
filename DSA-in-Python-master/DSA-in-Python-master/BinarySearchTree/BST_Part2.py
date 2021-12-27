# ------------------- Array representation of BST -----------

# We have seen the way to implement BST in python using the custom class implementation
# We can also use array/list to represent the BST
# First element should be root then enter elements from left to right at each level then move to another level and start again from left to right and so  on...
# BUT if there are scenarios where we dont have say left child of a parent and we have entered right child to the list then for left child , we have to leave previous element in the list empty to show
# that this left node is not present in the tree
# So, thumb rule is to start from left and add the nodes in the list. If there is any missing left node/child and there is a right node after that then add EMPTY to the list
# to show that particular node is missing otherwise this wont work.
# If at a particular level we have left child but not right then its fine because since we are going from left ot right then left should be there if right is present. Leave an element blnk in list to show this left node
# If we have added all the bnodes correctly then we can use below formulas to get the nodes:

# If a node is at index i where i is starting from 0
# Its left child is at 2*i + 1 positions
# Its right child is at 2*i + 2 positions
# Its parent is at i/2 -1 position if node is at even position
# its parent is at i//2 position if node is at odd position

# FULL BST is a tree which has all the maximum no of nodes present i.e. no position is vacant for a node at a particular level
# COMPLETE BST is a tree which don't have any missing elements while representing it in the list/Array form Hence, FULL tree is also a COMPLETE tree but reverse is not true
# or Complete tree is full till height/level N-1

# ---- Drawbacks of BST -----

# BST is mostly used for searching since it is organised in a tree structure where element < node is at left and > node is at right
# But for n elements, BST can be made in a muliple ways
# Minimum height of BST is logN and max height is n (which is a worst case scenario ) hence BST of O(n) is nothing but a kind of linear search
# O(N) is possible say when we are creating a skewed tree 40->30->20->10 now it is a sequential like tree with no right tree since all the elements are smaller than node
# this can be make like this  30->20->10->40 this is of height O(logN)
# So our objective is to make skewed BST of height n balanced so that they can be of height logN. For this AVL TREEs are used which we will discuss in next slide.

