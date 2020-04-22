# ------------------------------- AVL TREES ---------------------

# BST can have worst case complexity of O(n) when the tree becomes unbalanced. Unbalanced means when the balance factor is more than 1.
# BALANCE FACTOR for a node is the difference between the height of the left subtree and the height of the right subtree for that node.
#   balanceFactor(BF) =height(leftSubTree)−height(rightSubTree)
# If the balance factor is greater than zero then the subtree is left-heavy
# If the balance factor is less than zero then the subtree is right heavy.
# If the balance factor is zero then the tree is perfectly in balance

# Allowable balance factor is -1,1,0 so, any node having BF -1<=0<=1 can be said a balanced node and if it is outside this range then node is unbalanced and we can balance the nodes using ROTATIONS.
# Thus, we can say that if all the nodes of a tree are balanced then tree is AVL tree otherwise if any 1 node is out of -1<0<1 range then whole tree is unbalanced
# So,AVL can be balanced using ROTATIONS which can be performed only on 3 nodes doesn't matter how long is your tree (take 3 nodes at a time)
# 
