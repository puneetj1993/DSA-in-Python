"""
PS:- Shortest Common Supersequence
i/p: 2 strings X and Y
o/p: Length of shortest common supersequence
expected o/p: 9(aggxtxaxb)
"""

x="aggtab"
y="gxtxaxb"

m=len(x)
n=len(y)

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
    for j in range(1,n+1):
        # Choice diagram
        if x[i-1] == y[j-1]:
            t[i][j] = 1 + t[i-1][j-1]  
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1])
        
# Answer
# Shortest common supersequence is m+n-lcs
print(m+n-t[m][n])