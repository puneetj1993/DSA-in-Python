"""
PS:- MCM, GIven an array of matrix size , we have to find the total cost of all matrix multiplication i.e. A1*A2*A3*A4
I/P: An array containing the matrices size arr=[40,20,30,10,30]
O/P: Minimum cost of multiplication

"""

#------RECURSIVE CODE------------------

arr = [40,20,30,10,30]

i=1
j=len(arr)-1

min1 = 65536 #some high number

def solve(arr,i,j):

    # Base condition
    if i>=j:
        return 0
    
    # Loope to move k across the array
    for k in range(i,j):
    
        # Temp answer for each k
        temp_ans = solve(arr,i,k)+solve(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        
        # To store the minimum value as for loop proceeds
        global min1
        if temp_ans<min1:
            min1=temp_ans
        
    
    return temp_ans

solve(arr,i,j)
print("MInimum cost of MCM is", min1)

#------Top Down(Memoization) CODE------------------

arr = [40,20,30,10,30]
i=1
j=len(arr)-1

min1 = float('inf')

t = [[-1 for j in range(len(arr)+1)] for i in range(len(arr)+1)]

def solve(arr,i,j):
    if i>=j:
        return 0
    
    if t[i][j]!=-1:
        return t[i][j]
    global min1
    for k in range(i,j):
        temp_ans = solve(arr,i,k)+solve(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        if temp_ans<min1:
            min1=temp_ans
        t[i][j]=temp_ans
        return t[i][j]
solve(arr,i,j)
print(min1)