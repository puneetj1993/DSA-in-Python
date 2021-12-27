# Coin Change problem: Minimum no of coins to get the sum

arr = [1,2,3] #coin array
sum = 5
n=len(arr)
t = [[-1 for j in range(sum+1)] for i in range(n+1)]

# Initialization with Base Condition
# there is slight change in the initialization 
for i in range(n+1):
    for j in range(sum+1):
        if j == 0:
            t[i][j] = 0
        if i==0:
        # we are passing the highest possible value here as we need to minimize the no of coin. if we set 1 then ans migh come 1 only
            t[i][j] =sum+1  #Usually in questions, sum value range might be given, so, taken sum max value +1 to pass all the TCs

# Start loop from 1 as 0th row and 0th col is already handled with base condition
# Replace n with i and W with j
for i in range(1,n+1):
    for j in range(1,sum+1):
        if arr[i-1]<=j:
            op1 = 1+ t[i][j-arr[i-1]]  # As coin is included, did +1
            op2 = t[i-1][j]
            t[i][j] = min(op1,op2)      # Getting min of coins 
        elif arr[i-1]>j:
            t[i][j] = t[i-1][j]

print(t[n][sum])