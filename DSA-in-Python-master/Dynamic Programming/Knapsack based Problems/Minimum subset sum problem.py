# Minimum subset sum difference

arr = [1,2,7]
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
            t[i][j] = op1 or op2
        elif arr[i-1]>j:
            t[i][j] = t[i-1][j]

# Looping through the last row of table
# and adding only "True" sum values into the list
for j in range(sum1+1):
    if t[n][j]:
        lst.append(j)

# Minimum subset sum is min(range-2S1) or maximum S1 in half array i.e. sum(arr) - 2*lst[len(lst)//2 -1] element
print("Minimum subset sum difference", sum1-2*lst[len(lst)//2 -1])