# 0-1 Knapsack problem recurrsion
wt = [1,3,4,5]
val = [1,4,5,7]
W=7
n=len(wt)

def knapsack(wt,val,W,n):
    
    # Base condition
    # if n=0 or weight of bag is zero
    # then we can't add any item, return 0
    if n ==0 or W ==0:
      return 0
    
     # if wt of any item is<= total capacity then
    # we have 2 options, either to add or not add
    if wt[n-1]<=W:
        op1 = val[n-1]+ knapsack(wt,val,W-wt[n-1],n-1)
        op2 = knapsack(wt,val,W,n-1)
        return max(op1,op2)
    
    # if wt of any item is>total capacity then
    # we have only option to not add it    
    elif wt[n-1] > W:
        op3 = knapsack(wt,val,W,n-1)
        return op3

print(knapsack(wt,val,W,n))

#--------------Recurrsion with Memoization = DP(Top-Down approach) -------------

wt = [1,3,4,5]
val = [1,4,5,7]
W=7
n=len(wt)

# Creating  n*m matrix for memoization
# here n=n and m=W as these 2 are only changing arguments
# Mostly we have given a constraint value for n and W
# take that max value to create 2d array
# And intialize the complete matrix with -1 in each cell
t = [[-1 for i in range(20)] for j in range(20)]

def knapsack(wt,val,W,n):
    
    if n ==0 or W ==0:
      return 0
    
    # if recurssion call to t[n][W] exists in matrix
    # then return the value and stop the recurssion call
    if t[n][W]!= -1:
        return t[n][W]
    
    #If not, then save the data in matrix for current
    # n and W
    if wt[n-1]<=W: 
        op1 = val[n-1]+ knapsack(wt,val,W-wt[n-1],n-1)
        op2 = knapsack(wt,val,W,n-1)
        t[n][W] = max(op1,op2)
        return t[n][W]
        
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt,val,W,n-1)
        return t[n][W]

print(knapsack(wt,val,W,n))

#---------------------Bottom UP Approach -------------
# 0-1 Knapsack problem recurrsion

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
            op1 = val[i-1]+ t[i-1][j-wt[i-1]]
            op2 = t[i-1][j]
            t[i][j] = max(op1,op2)
            
        elif wt[i-1] > j:
            t[i][j] = t[i-1][j]

# Answer will be at n and W            
print("Max Profit is", t[n][W])