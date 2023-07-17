# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        i = 0
        sign = 1 # +ve

        while s[i] == ' ':
            i += 1
        
        if i < len(s) and s[i] == '-' or s[i] == '+':
            sign = 1 if s[i] == '+' else -1
            i += 1

        while i< len(s) and s[i].isdigit():
            if num > 2147483647 // 10 or num == 2147483647 // 10 and ord(s[i]) > ord('7'):
                return -2147483647 if sign == -1 else 2147483647

            num = num * 10 + (ord(s[i]) - ord('0'))
            i += 1
        
        return num * sign