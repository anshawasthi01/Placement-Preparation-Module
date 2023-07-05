# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, arr: List[List[int]], target: int) -> bool:

        rows = len(arr)
        cols = len(arr[0])
        s, e = 0, rows*cols - 1
        mid = s + (e-s)//2

        while s <= e:
            rowIndex = mid//cols
            colIndex = mid%cols
    
            if arr[rowIndex][colIndex] == target:
                print("Found at ", rowIndex, " ", colIndex)
                return True
    
            if arr[rowIndex][colIndex] < target:
                s = mid +1

            else:
                e = mid - 1
            mid = s + (e-s)//2
        return False
    
        # n = len(matrix)
        # m = len(matrix[0])
        # i = 0
        # j = m-1
        
        # while i!=n and j!=-1:
        #     if matrix[i][j]>target:
        #         j-=1
        #     elif matrix[i][j]<target:
        #         i+=1
        #     else:
        #         return True
        # return False