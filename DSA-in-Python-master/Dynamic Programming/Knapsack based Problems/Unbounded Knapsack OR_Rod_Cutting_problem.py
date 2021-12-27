#---------------------Bottom UP Approach -------------
# Unbounded  Knapsack problem 

wt = [1,3,4,5]
val = [1,4,5,7]
W=7
n=len(wt)

t = [[-1 for i in range(W+1)] for j in range(n+1)]

#Initializing the table with base condition
# that if n==0 or w==0, return 0
for i in range(n+1):
    for j in range(W+1):
        if i==0 or j==0:
            t[i][j]=0

# Start loop from 1 as 0th row and 0th col is already handled with base condition
# Replace n with i and W with j
for i in range(1,n+1):
    for j in range(1,W+1):
        if wt[i-1]<=j: 
            op1 = val[i-1]+ t[i][j-wt[i-1]]  # If item is included, multiple occurences possible, so we are taking ith item again insted of i-1
            op2 = t[i-1][j] # item is not included, so, it's processed and move to i-1th item
            t[i][j] = max(op1,op2)
            
        elif wt[i-1] > j:
            t[i][j] = t[i-1][j] #similarly, item is processed as it is excluded

# Answer will be at n and W            
print("Max Profit is", t[n][W])