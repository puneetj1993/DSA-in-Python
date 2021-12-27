"""
Sum of subset problem
PS: An array is given and sum is given , we have to find all the combinations in which sum of elements of list is equal to given sum
IP: arr and sum m
840 steps
"""

------- Using recurrsion solved in 840 steps ------------

arr = [5,10,12,13,15,18]
m=30
op = 0
ip = sum(arr)
result=[]

def solve(arr,op,ip):
    
    # If op i.e. sum of elements till now =
    # m then print result list which contains
    # the elements which are included
    if op == m:
        print(result)
        return
    
    # If len(arr) is empty it means all the data points are
    # used then return nothing or if sum till now is greater the m
    # then also return nothing to stop 
    if len(arr) == 0 or op>m:
        return
    
    # Two case, include the 0th element of current list
    # or exclude it
    op1 = op
    op2 = op
    
    # Case1 - include
    # new output will be old + arr[0]
    # new input would be old - arr[0] as we included it
    op1 = op1 + arr[0]
    ip1 = ip - arr[0]
    
    # As element is included, adding in list
    # smalling the input arr i.e. arr[1:]
    result.append(arr[0])
    solve(arr[1:],op1,ip1)
    
    # Case 2 - Exclude
    # code will reach here if we return nothing as in case of
    # op>m. so, we need to exclude this
    # thats why removing the last element from result as we are excluding it
    result.pop()
    
    # As element is excluded so, new op2 will remain as old op
    # but ip2 will be smaller and also array
    ip2 = ip - arr[0]
    solve(arr[1:],op2,ip2)

solve(arr,op,ip)

----- Using Backtracking solved in 580 steps------

arr = [5,10,12,13,15,18]
m=30
op = 0
ip = sum(arr)
result=[]
solution=[]

def solve(arr,op,ip):
    
    # If op i.e. sum of elements till now =
    # m then add result list which contains
    # the elements which are included to solution list
#Note: please make sure to use either result[:] or copy.deepcopy(result)
# otherwise if you use result directly then reference to it got appended
# in solution list and anyfurther changes in result list will reflect here which
# is not desired
    if op == m:
        solution.append(result[:])
        return
    
    # Loop
    for i in range(len(arr)):
        
        # Bounding function or constraint
        if len(arr) == 0 or op>m:
            break
        #Include case 
        op1 = op + arr[i]
        ip1 = ip - arr[i]
        result.append(arr[i])
        solve(arr[i+1:],op1,ip1)
        #Exclude case
        result.pop()
    return

solve(arr,op,ip)
print(solution)