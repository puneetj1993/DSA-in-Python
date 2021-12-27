"""
The following is a description of the instance of this famous puzzle involving n=2 eggs and a building with k=36 floors.
Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and which will cause the eggs to break on landing. We make a few assumptions:
…..An egg that survives a fall can be used again. 
…..A broken egg must be discarded. 
…..The effect of a fall is the same for all eggs. 
…..If an egg breaks when dropped, then it would break if dropped from a higher floor. 
…..If an egg survives a fall then it would survive a shorter fall. 
…..It is not ruled out that the first-floor windows break eggs, nor is it ruled out that the 36th-floor do not cause an egg to break.
If only one egg is available and we wish to be sure of obtaining the right result, the experiment can be carried out in only one way. Drop the egg from the first-floor window; if it survives, drop it from the second-floor window. Continue upward until it breaks. In the worst case, this method may require 36 droppings. Suppose 2 eggs are available. What is the least number of egg-droppings that is guaranteed to work in all cases? 
The problem is not actually to find the critical floor, but merely to decide floors from which eggs should be dropped so that the total number of trials are minimized.
"""
import sys

e = 2
f = 10
    
# Function to get minimum number of trials
# needed in worst case with e eggs and f floors
def eggDrop(e, f):
 
    # If there are no floors, then no trials
    # needed. OR if there is one floor, one
    # trial needed.
    if (f == 1 or f == 0):
        return f
 
    # We need f trials for one egg
    # and f floors
    if (e == 1):
        return f
 
    min = sys.maxsize
 
    # Consider all droppings from 1st
    # floor to kth floor and return
    # the minimum of these values plus 1.
    for x in range(1, f + 1):
        
        # Here, in first condition if egg is broken then e=e-1 and we will not got higher as if it gets broken at x then will also gets broken at x+1
        #so, we will check till x-1 floors
        #2nd condition: if egg is not broken at xth floor then we will go higher and check for remaining floors which are f-x
        #Max is used here to get the worst case scenario
        res = 1 + max(eggDrop(e - 1, x - 1), eggDrop(e, f - x))
        if (res < min):
            min = res
 
    return min
 
    
print("Minimum number of trials in worst case with",
       e, "eggs and", f, "floors is", eggDrop(e, f))
       
#------------------Top Down  Memoized------------------
import sys

e = 2
f = 10

MAX=1000

t = [[-1 for j in range(MAX)]for i in range(MAX)]

# Function to get minimum number of trials
# needed in worst case with e eggs and f floors
def eggDrop(e, f):

    if t[e][f] != -1:
        return t[e][f]
 
    # If there are no floors, then no trials
    # needed. OR if there is one floor, one
    # trial needed.
    if (f == 1 or f == 0):
        return f
 
    # We need k trials for one egg
    # and k floors
    if (e == 1):
        return k
 
    min = sys.maxsize
 
    # Consider all droppings from 1st
    # floor to kth floor and return
    # the minimum of these values plus 1.
    for x in range(1, k + 1):
 
        res = 1 + max(eggDrop(e - 1, x - 1),  # Used max here as we have to find the worst case scenarios
                  eggDrop(e, f - x))
        if (res < min):
            min = res
    
    t[e][f] = min
    return t[e][f]
 
    
print("Minimum number of trials in worst case with",
       e, "eggs and", f, "floors is", eggDrop(e, f))

#------------------Top Down Extra Memoized------------------

import sys

e = 2
f = 10

MAX=1000

t = [[-1 for j in range(MAX)]for i in range(MAX)]

# Function to get minimum number of trials
# needed in worst case with e eggs and f floors
def eggDrop(e, f):

    if t[e][f] != -1:
        return t[e][f]
 
    # If there are no floors, then no trials
    # needed. OR if there is one floor, one
    # trial needed.
    if (f == 1 or f == 0):
        return f
 
    # We need k trials for one egg
    # and k floors
    if (e == 1):
        return k
 
    min = sys.maxsize
 
    # Consider all droppings from 1st
    # floor to kth floor and return
    # the minimum of these values plus 1.
    for x in range(1, k + 1):
        if t[e-1][x-1] != -1:
            lower = t[e-1][x-1]
        else:
            lower = eggDrop(e - 1, x - 1)
            t[e-1][x-1] = lower
        
        if t[e-1][f-x] != -1:
            upper = t[e-1][f-x]
        else:
            upper = eggDrop(e, f - x)
            t[e-1][x-1] = upper
            
 
        res = 1 + max(lower, upper)  # Used max here as we have to find the worst case scenarios

        if (res < min):
            min = res
    
    t[e][f] = min
    return t[e][f]
 
    
print("Minimum number of trials in worst case with",
       e, "eggs and", f, "floors is", eggDrop(e, f))
