# Count the number of subset with given sum

arr = [1,1,2,3]
sum1= sum(arr)
n=len(arr)
lst=[]

t = [[-1 for j in range(sum1+1)] for i in range(n+1)]

# Initialization with Base Condition

for i in range(n+1):
    for j in range(sum1+1):
        if i == 0:
            t[i][j] = 0
        if j==0:
            t[i][j] = 1

# Start loop from 1 as 0th row and 0th col is already handled with base condition
# Replace n with i and W with j
for i in range(1,n+1):
    for j in range(1,sum1+1):
        if arr[i-1]<=j:
            op1 = t[i-1][j-arr[i-1]]
            op2 = t[i-1][j]
            t[i][j] = op1 + op2  # Just change or to + as we need to have count
        elif arr[i-1]>j:
            t[i][j] = t[i-1][j]

print(t[n][w])