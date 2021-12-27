# ------------------------------- AVL TREES ---------------------

# BST can have worst case complexity of O(n) when the tree becomes unbalanced. Unbalanced means when the balance factor is more than 1.
# BALANCE FACTOR for a node is the difference between the height of the left subtree and the height of the right subtree for that node.
#   balanceFactor(BF) =height(leftSubTree)−height(rightSubTree); here we are calaculating the max height not the no of nodes on say left subtree 
# If the balance factor is greater than zero then the subtree is left-heavy
# If the balance factor is less than zero then the subtree is right heavy.
# If the balance factor is zero then the tree is perfectly in balance
# So, AVL Tree is a self balancing binary search tree

# Allowable balance factor is -1,1,0 so, any node having BF -1<=0<=1 can be said a balanced node and if it is outside this range then node is unbalanced and we can balance the nodes using ROTATIONS.
# Thus, we can say that if all the nodes of a tree are balanced then tree is AVL tree otherwise if any 1 node is out of -1<0<1 range then whole tree is unbalanced
# So,AVL can be balanced using ROTATIONS which can be performed only on 3 nodes doesn't matter how long is your tree (take 3 nodes at a time)
# There are total 4 types of ROTATIONS - LL LR RL RR
# LL - Left of Left; it a single rotation rotating the unbalanced node in the right direction. LL means right subtree
# LR - Left of right; It a 2 rotations ; first is left rotation and then right rotation to make it balanced.Left of right means node is unbalanced in the direction of left and then left from the root menas in the left sub tree and then right child of a node
# RL - Right of Left: Its also a 2 rotations; first in right and then left. Right of Left means node is unbalanced in the direction of right and then left from the root menas in the right sub tree
# RR - Right of Right; it's also a single rotation rotating the unbalanced node in the left direction. RR means right subtree

#--------- How to create AVL tree ---------------------

# Whenever we are adding nodes to the tree, it is good practice to check BF after adding each node and if there is any unbalanced nodes then make it balanced using the rotations and then add further nodes.
# So, we have to check BF after adding each node and make necessary changes by rotating the nodes to get the balanced final tree.
# If there are 2 nodes which get unbalanced after inserting a node then node which is closest to LEAF node has to be taken care first.
# After modifying the closest node( or farthest from ROOT) then again check BF and if other one is also balanced due to this closest node rotation then there is no need to perform rotations again.
# As mentioned above, rotation can be performed only on 3 nodes at a time.
# Type of rotation depends on the direction of node from root like if node is a right child of a left child of root then it LR (from root) so we will perform LR rotation
# There may be a scenario where we have to perform rotations on 3 nodes which have sub tree attach to them , in this case forget about the subtree and rotate the nodes as usual and then attach subtrees accordingly post rotation.
