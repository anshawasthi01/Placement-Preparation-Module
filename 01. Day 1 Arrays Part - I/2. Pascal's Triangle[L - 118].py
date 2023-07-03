# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
       

        res=[[1]]
        for i in range(1,numRows):
            arr=[0]*(i+1)
            arr[0]=arr[i]=1
            preArr=res[-1]
            for j in range(1,(i//2)+1):
                arr[j]=arr[i-j]=preArr[j]+preArr[j-1]
            res.append(arr)
        return res
        