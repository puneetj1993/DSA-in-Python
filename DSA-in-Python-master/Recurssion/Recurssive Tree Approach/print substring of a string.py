"""
Print all the substrings of any given string
Input: 
    - ip Given string ip="ab"
Output:-
    - op, all possible substrings of ip i.e. "","a","b","ab"
"""

#Initial data

ip = "ab"
op=""


def solve(ip,op):
    # IN RECURSSIVE TREE APPROACH, OUTPUT IS OBTAINED ONCE THE INPUT IS EMPTY
    # SO, CHECKING THE SAME IF LENGTH OF IP STRING IS EMPTY,PRINT OUTPUT AND END THE FUNCTION CALL
    if not len(ip):
        print(op)
        return
    # output1 and output2 are same as output
    op1=op
    op2=op
    
    # Now, if say ip[0]=a is considered then op should include a
    # so, handling this
    # op1 means 'a' is not included
    # op2 means 'a' is included
    op2= op2 + ip[0]
    
    # Now, once we got the op1and op2, we will make the input smaller by removing the
    # 0th element as it is already included in the op2
    ip=ip[1:]
    
    # Now, calling th solve again on smaller input and 2 smaller outputs
    solve(ip,op1)
    solve(ip,op2)

# Calling solve function on ip and op
solve(ip,op)
    
    