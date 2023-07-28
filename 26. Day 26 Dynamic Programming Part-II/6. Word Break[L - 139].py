# https://leetcode.com/problems/word-break/

class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def check(s, wordDict):
            if s in memo:
                return memo[s]

            if s == '':
                return True

            for word in wordDict:
                if s.startswith(word):
                    suffix = s[len(word):]
                    if check(suffix, wordDict):
                        memo[word] = True
                        return True


            memo[s] = False
            return False
    
        return check(s, wordDict)