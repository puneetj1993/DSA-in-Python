# Count the number of subset with given difference

arr = [1,1,2,3]
diff = 1
sum1= sum(arr)
n=len(arr)
lst=[]

t = [[-1 for j in range(sum1+1)] for i in range(n+1)]

# Initialization with Base Condition

for i in range(n+1):
    for j in range(sum1+1):
        if i == 0:
            t[i][j] = False
        if j==0:
            t[i][j] = True

# Start loop from 1 as 0th row and 0th col is already handled with base condition
# Replace n with i and W with j
for i in range(1,n+1):
    for j in range(1,sum1+1):
        if arr[i-1]<=j:
            op1 = t[i-1][j-arr[i-1]]
            op2 = t[i-1][j]
            t[i][j] = op1 + op2
        elif arr[i-1]>j:
            t[i][j] = t[i-1][j]

# Till here, table is completely populated.
# we have to get the count of all the subsets where sum=s1
s1 = (sum(arr)+diff)//2
print(t[n][s1])