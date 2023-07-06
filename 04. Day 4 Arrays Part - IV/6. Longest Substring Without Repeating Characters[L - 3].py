# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)==0:
            return 0       

        map = {}
        start = l_str = 0
        
        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]]+1            
            else:
                l_str = max(l_str, i-start+1)
            map[s[i]] = i

        return l_str
