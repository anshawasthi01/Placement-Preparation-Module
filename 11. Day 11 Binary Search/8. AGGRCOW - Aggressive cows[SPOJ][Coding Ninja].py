# Coding Ninja : https://www.codingninjas.com/studio/problems/aggressive-cows_1082559?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
# SPOJ : https://www.spoj.com/submit/AGGRCOW/

from typing import List

def isCompatible(inp: List[int], dist: int, cows: int) -> bool:
    n = len(inp)
    k = inp[0]
    cows -= 1
    for i in range(1, n):
        if inp[i] - k >= dist:
            cows -= 1
            if not cows:
                return True
            k = inp[i]
    return False

def largestMinimumDistance(inp: List[int], cows: int) -> int:
    inp.sort()
    maxD = inp[-1] - inp[0]
    ans = float('-inf')
    for d in range(1, maxD + 1):
        possible = isCompatible(inp, d, cows)
        if possible:
            ans = max(ans, d)
    return ans

if __name__ == '__main__':
    inp = [1, 2, 8, 4, 9]
    cows = 3
    print(
        f"The largest minimum distance is {largestMinimumDistance(inp, cows)}")