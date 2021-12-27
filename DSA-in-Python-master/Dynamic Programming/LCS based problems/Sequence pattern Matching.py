"""
PS:- Sequence Pattern Matching. 2 strings are given and we have to check if a sequence is present in b
I/P: 2 string X and Y
O/P: True if sequence is present otherwise False
expected o/p: True
"""
x="AXY"
y = "ADXCPY"


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
# If LCS == a.length
if m==t[m][n]:
    print("true")
else:
    print("false")