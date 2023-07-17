# https://leetcode.com/problems/longest-palindromic-substring/

def isPalindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if isPalindrome(s, i, j):
                    t = s[i:j-i+1]
                    if len(t)>len(ans):
                        ans = t

                    # ans = t if len(t)>len(ans) else ans
        return ans


        # start=0
        # maxLen=1
        # for i in range(1,len(S)):
        #     #even
        #     l=i-1 
        #     r=i   
        #     print(l,r)
        #     while l>=0 and r<len(S) and S[l]==S[r]:
        #         if r-l+1>maxLen:
        #             maxLen=r-l+1
        #             start=l
        #         l-=1
        #         r+=1
        #     #odd    
        #     l=i-1
        #     r=i+1
        #     while l>=0 and r<len(S) and S[l]==S[r]:
        #         if r-l+1>maxLen:
        #             maxLen=r-l+1
        #             start=l
        #         l-=1
        #         r+=1    
                
            
        # return S[start:start+maxLen]  