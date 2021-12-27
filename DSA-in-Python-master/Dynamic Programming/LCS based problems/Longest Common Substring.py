"""
PS:- Longest Common Substring - Bottom Up (iterative)
i/p: 2 strings X and Y
o/p: LCS i.e. length of longest common substring
expected o/p: 3 (abc)
"""

x="abcde"
y="abcfde"

m=len(x)
n=len(y)

maxval =0
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
            maxval=max(maxval,t[i][j])  #Storing the max length out of all possible ans
        else:
            t[i][j] = 0 # if not equal then we don't wish to include it hence 0
        
# Answer
print(maxval)