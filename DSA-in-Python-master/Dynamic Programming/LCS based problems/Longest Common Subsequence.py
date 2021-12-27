"""
PS:- Longest Common Subsequence LCS - Recurrsion
i/p: 2 strings X and Y
o/p: LCS i.e. length of longest common subsequence
expected o/p: 4 (abdh)
"""

x="abcdgh"
y="abedfhr"

m=len(x)
n=len(y)


def lcs(x,y,m,n):
    
    # Base condition
    if m == 0 or n ==0:
        return 0
    
    # Choice diagram
    if x[m-1] == y[n-1]:
        return 1 + lcs(x,y,m-1,n-1)
    else:
        return max(lcs(x,y,m-1,n),lcs(x,y,m,n-1))
# Answer
print(lcs(x,y,m,n))

---------------------------------Top down memoization-----------------------------
"""
PS:- Longest Common Subsequence LCS - Top Down(Memoization)
i/p: 2 strings X and Y
o/p: LCS i.e. length of longest common subsequence
expected o/p: 4 (abdh)
"""

x="abcdgh"
y="abedfhr"

m=len(x)
n=len(y)

# A matrix of t[m+1][n+1] with base value of -1
t = [[-1 for j in range(n+1)] for i in range(m+1)]

def lcs(x,y,m,n):

    # Base condition
    if m == 0 or n ==0:
        return 0
    
    # if function call exists in table, directly return it
    if t[m][n] != -1:
        return t[m][n]
    
    # Choice diagram
    if x[m-1] == y[n-1]:
        t[m][n] =  1 + lcs(x,y,m-1,n-1)
        return t[m][n]
    else:
        t[m][n] = max(lcs(x,y,m-1,n),lcs(x,y,m,n-1))
        return t[m][n]
# Answer
print(lcs(x,y,m,n))

---------------------------------Bottom Up iterative-----------------------------
"""
PS:- Longest Common Subsequence LCS - Bottom Up(Iterative)
i/p: 2 strings X and Y
o/p: LCS i.e. length of longest common subsequence
expected o/p: 4 (abdh)
"""

x="abcdgh"
y="abedfhr"

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
            t[i][j] =  1 + t[i-1][j-1]
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1])
        
# Answer
print(t[m][n])