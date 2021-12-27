"""
Problem Statement: N queens problem using Back tracking 
I.P: A chess board of N*N size
O.P: Correct position of N queens
"""


def is_safe(board,r,c):
    
    # To check if any Q already exists on the 
    #  this row r by checking all the column
    # representing by i i.e for n=4, 0 to 3
    for i in range(len(board)):
        if board[r][i] == 1:
            return False
    
    # To check if any Q already exists on the 
    # this column by checking all the rows
    # representing by i i.e for n=4, 0 to 3
    for i in range(len(board)):
        if board[i][c] == 1:
            return False
            
    # To check if any Q already exists on the 
    # '\' diagonal by checking all the rows and columns
    # before the point(r,c) at which we're checking 
    (i,j)=(r,c)
    while i >= 0 and j >= 0:
        if board[i][j]==1:
            return False
        i=i-1
        j=j-1
    
    # To check if any Q already exists on the 
    # '/' diagonal by checking all the rows before
    # the point(r,c) and column after it. It is becos
    # we are adding Q row wise
    (i,j)=(r,c)
    while i >= 0 and j < len(board):
        if board[i][j]==1:
            return False
        i=i-1
        j=j+1
    
    return True  

def solve(board,r):
    
    # We are adding Q row wise so, if all the rows
    # have been filled then it is the answer
    if r>=len(board):
        print(board)
        return
    
    
    for i in range(len(board)):
        
        # If it's safe to put Q at r,c then put it 
        # by assigning value 1 to that cell.
        if is_safe(board,r,i):
            
            board[r][i] = 1
            #once Q is placed for this row, increment
            #the row number
            solve(board,r+1)
            
            # backtrack and remove the queen
            # from the current cell
            board[r][i] = 0
    
    return 

n=4
board = [[0 for i in range(n)] for j in range(n)]

solve(board,0)