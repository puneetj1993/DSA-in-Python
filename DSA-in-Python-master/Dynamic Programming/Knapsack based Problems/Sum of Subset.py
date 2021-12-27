# Sum of subsets

arr = [2,3,7,8,10]
sum= 11
n=len(arr)

t = [[-1 for j in range(sum+1)] for i in range(len(arr)+1)]

# Initialization with Base Condition

for i in range(n+1):
    for j in range(sum+1):
        if i == 0:
            t[i][j] = False
        if j==0:
            t[i][j] = True

# Start loop from 1 as 0th row and 0th col is already handled with base condition
# Replace n with i and W with j
for i in range(1,n+1):
    for j in range(1,sum+1):
        if arr[i-1]<=j:
            op1 = t[i-1][j-arr[i-1]]
            op2 = t[i-1][j]
            t[i][j] = op1 or op2
        elif arr[i-1]>j:
            t[i][j] = t[i-1][j]
print(t[n][sum])