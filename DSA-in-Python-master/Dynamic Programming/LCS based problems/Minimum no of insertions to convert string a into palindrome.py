"""
PS:- Minimum # of insertion required to convert string into Palindrome
I/P: 1 string X 
O/P: Print the minimum insertions required
expected o/p: 2
"""

# Here only 1 string is given but for LCS we should have 2 strings
# so, we have to derive second string.
# If we take y=reverse(x) then LCS of x and y is LPS
x="AEBCBDA"

y = x[::-1]


m=len(x)
n=len(y)
res=""
# A matrix of t[m+1][n+1] with base value of -1
t = [[-1 for j in range(n+1)] for i in range(m+1)]

# Initialization of table with base condition
for i in range(m+1):
    for j in range(n+1):
        if i==0:
            t[i][j] = 0
        if j==0:
            t[i][j] = 0

for i in range(1,m+1):
    for j in range(1,n+1):        # Choice diagram
        if x[i-1] == y[j-1]:
            t[i][j] = 1 + t[i-1][j-1]  
        else:
            t[i][j] = max(t[i-1][j], t[i][j-1])
            
# Answer
# Minimum number of insertions required is also same as deletions which is len(x) - LPS
print(m-t[m][n])