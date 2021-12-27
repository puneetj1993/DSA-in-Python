"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Below is one possible representation of A = “great”:
 great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node “gr” and swap its two children, it produces a scrambled string “rgeat”.

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that “rgeat” is a scrambled string of “great”.

Similarly, if we continue to swap the children of nodes “eat” and “at”, it produces a scrambled string “rgtae”.

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that “rgtae” is a scrambled string of “great”.
"""

S1 = "coder"
S2 = "ocred"


def isScramble(S1, S2):
     
    # Strings of non-equal length
    # cant' be scramble strings
    if len(S1) != len(S2):
        return False
 
    n = len(S1)
 
    # Empty strings are scramble strings
    if not n:
        return True
 
    # Equal strings are scramble strings
    if S1 == S2:
        return True
 
    # Check for the condition of anagram
    if sorted(S1) != sorted(S2):
        return False
 
    for i in range(1, n):
         """
        There are 2 conditions(sub problems) here
        1) If we swap the non leaf nodes: then we will check if 
            string before partition(which is represented by i) before swap == string after partition after swap 
            String after partiotion before swap = String before partions after swap
        
        1) If we don't swap the non leaf nodes: then we will check if 
            string before partition before swap == string before partition after swap 
            String after partiotion before swap = String after partions after swap as swap wasn't done
         
         """
        # Check if S2[0...i] is a scrambled
        # string of S1[0...i] and if S2[i+1...n]
        # is a scrambled string of S1[i+1...n]
        if (isScramble(S1[:i], S2[:i]) and
            isScramble(S1[i:], S2[i:])):
            return True
 
        # Check if S2[0...i] is a scrambled
        # string of S1[n-i...n] and S2[i+1...n]
        # is a scramble string of S1[0...n-i-1]
        if (isScramble(S1[-i:], S2[:i]) and
            isScramble(S1[:-i], S2[i:])):
            return True
 
    # If none of the above
    # conditions are satisfied
    return False
     
if (isScramble(S1, S2)):
    print("Yes")
else:
    print("No")
 
 #-------------------------------------Top Down memoized-----------------------
 
S1 = "coder"
S2 = "ocred"
map={}

def isScramble(S1, S2):
     
    # Strings of non-equal length
    # cant' be scramble strings
    if len(S1) != len(S2):
        return False
 
    n = len(S1)
 
    # Empty strings are scramble strings
    if not n:
        return True
 
    # Equal strings are scramble strings
    if S1 == S2:
        return True
 
    # Check for the condition of anagram
    if sorted(S1) != sorted(S2):
        return False
     
    # Checking if both Substrings are in
    # map or are already calculated or not
    # we are using map here instead of DP matrix
    if map.get(S1+' '+S2,0):
        return map[S1+' '+S2]
    
    # Declaring a flag variable
    flag = False
 
    for i in range(1, n):
         """
        There are 2 conditions(sub problems) here
        1) If we swap the non leaf nodes: then we will check if 
            string before partition(which is represented by i) before swap == string after partition after swap 
            String after partiotion before swap = String before partions after swap
        
        1) If we don't swap the non leaf nodes: then we will check if 
            string before partition before swap == string before partition after swap 
            String after partiotion before swap = String after partions after swap as swap wasn't done
         
         """
        # Check if S2[0...i] is a scrambled
        # string of S1[0...i] and if S2[i+1...n]
        # is a scrambled string of S1[i+1...n]
        if (isScramble(S1[:i], S2[:i]) and
            isScramble(S1[i:], S2[i:])):
            flag = True
            return True
 
        # Check if S2[0...i] is a scrambled
        # string of S1[n-i...n] and S2[i+1...n]
        # is a scramble string of S1[0...n-i-1]
        if (isScramble(S1[-i:], S2[:i]) and
            isScramble(S1[:-i], S2[i:])):
            flag = True
            return True
    
    # Storing calculated value to map
    map[S1+" "+S2] = flag
 
    # If none of the above
    # conditions are satisfied
    return False
     
if (isScramble(S1, S2)):
    print("Yes")
else:
    print("No")