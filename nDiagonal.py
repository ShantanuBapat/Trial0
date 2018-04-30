# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
def nDiag(square=np.array([]),n=1):
    count = 0
    #print("Entering" + str(square))
    if(square.size != n*n):
        #print("Setting init array")
        square = np.ones((n,n))*-10
    if( not np.any(square == -10)):
        print(square)
        return 1
    #print(square)
    for i in range(n):
        for j in range(n):
            #print("i = %d , j = %d" %(i,j))
            if(square[i][j] == -10):
                if(checkIfAllowed(square,i,j,1)):
                    square[i][j] = 1
                    #print(square)
                    count += nDiag(square.copy(),n)
                #if(checkIfAllowed(square,i,j,0)):
                square[i][j] = 0
                count += nDiag(square.copy(),n)
                
                square[i][j] = -10
                if(checkIfAllowed(square,i,j,-1)):
                    square[i][j] = -1
                    count += nDiag(square.copy(),n)
                return count
                
            
def nDiag1(square=np.array([]),n=1):
    #print("Entering" + str(square))
    if(square.size != n):
        print("Setting init array")
        square = np.ones((n))*-10
    if( not np.any(square == -10)):
        print(square)
        return
    #print(square)
    for i in range(n):
        if(square[i] == -10):
            square[i] = 1
            #print(square)
            nDiag1(square.copy(),n)
            square[i] = 0
            nDiag1(square.copy(),n)
            return
            
            
def extend(perm, n):
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)
            #if can_be_extended_to_solution(perm):
            extend(perm, n)
            perm.pop()

#extend(perm = [], n = 20)

def checkIfAllowed(square,row,col,val):
    r1,c1 = square.shape
    r1 -= 1
    c1 -= 1
    #return True
#    if((col-1) < 0):
#        return True
#    else:
#        if square[row][col-1] == val :
#            return False
#    return True
    #(-1,1)
    if not (((row-1) < 0) or ((col+1) > c1)):
        if((square[row-1][col+1] == 1) and (val == 1)):
            return False
    #(1,-1)
    if not (((row+1) > r1) or ((col-1) < 0)):
        if((square[row+1][col-1] == 1) and (val == 1)):
            return False

    #(-1,0)
    if not ((row-1) < 0):
        if((square[row-1][col] == -1) and (val == 1)):
            return False
        if((square[row-1][col] == 1) and (val == -1)):
            return False
    #(0,-1)
    if not ((col-1) < 0):
        if((square[row][col-1] == -1) and (val == 1)):
            return False
        if((square[row][col-1] == 1) and (val == -1)):
            return False
    #(1,1)
    if not (((row+1) > r1) or ((col+1) > c1)):
        if((square[row+1][col+1] == -1) and (val == -1)):
            return False
    #(-1,-1)
    if not (((row-1) < 0) or ((col-1) < 0)):
        if((square[row-1][col-1] == -1) and (val == -1)):
            return False
    #(1,0)
    if not ((row+1) > r1):
        if((square[row+1][col] == -1) and (val == 1)):
            return False
        if((square[row+1][col] == 1) and (val == -1)):
            return False
    #(0,1)   
    if not ((col+1) > c1):            
        if((square[row][col+1] == -1) and (val == 1)):
            return False
        if((square[row][col+1] == 1) and (val == -1)):
            return False
    return True    