# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # CODE HERE
        m, n = len(matrix), len(matrix[0])
                #row            # column
   
        r, c = False, False
   
    # iterate through matrix to mark the zero row and cols
        for j in range(n):
            if matrix[0][j] == 0:
                r = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                c = True
                break
    
    # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        

        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j]=0

        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j]=0

    # update the first r and c if they're zero

        if c:
            for i in range(m):
                matrix[i][0]=0

        if r:
            for j in range(n):
                matrix[0][j]=0
        return matrix
