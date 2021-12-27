"""
We are using Backtracking aproach here

Problem Statement: 
Find all the permutations of the given list/array
Input: arr=[1,2,3]
Output: all possible permutations of the given input (there will 3!=6 permutations)
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]

"""


arr=[1,2,3]

def solve(arr):
  
    if len(arr) == 1:
        return [arr]
        
    result=[]    
    
    for i in range(len(arr)):
       n = arr[i]
       ip = arr[:i] + arr[i+1:]
       res = solve(ip)

       for i in res:
           result.append([n] + i)
    return result
 
 
# Driver program to test above function
for p in solve(arr):
    print(p)
    


Another solution as per Recursion tree:

ip=['1','2','3']
op=""
def solve(ip,op):
  
    # If ip is empty then it means we have got 
    # the output hence, printing it
    if not len(ip):
        print(op)
        return

    for i in range(len(ip)):
        
        # assiging the old output the new output
        # carry forwarding the output(say, op=1)
        op1 = op
        
        # Merging the old output with the newly
        # selected input(say op1 = '1'+'2')
        op1=op1 + ip[i]
        
        #Additional thing that if constraint is applied that 3 can't sit in middle
        if len(op)>1 and op1[1]=='3':
            break
        
        # Smalling the input(say [2,3] to [3] as we hve
        # selected 2 above(if 3 is slected then, [3,2] to [2]
        arr=ip[:i]+ ip[i+1:]
        
        #passing the smaller input
        #We can't pass the ip here as we need to keep the original ip
        # input intact
        solve(arr,op1)
 

solve(ip,op)
