"""
PS:- Minimum # of insertions and deletions required to convert
   string "a" to string "b"
i/p: 2 strings x and y
o/p: int (insertion and deletion count)
expected o/p: 1 2 
"""

x="heap"
y="pea"

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
            t[i][j] = max(t[i-1][j], t[i][j-1])
        
# Answer
# Minimum No of deletions = m - LCS
# Minimum number of insertions = n - LCS
print({m-t[m][n]}," deletions, ",{n-t[m][n]}," insertions")