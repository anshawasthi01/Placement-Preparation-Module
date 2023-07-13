# https://www.codingninjas.com/studio/problems/1062679?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

def multiply(number, n):
    ans = 1.0
    for i in range(1, n + 1):
        ans = ans * number
    return ans


def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    low = 1
    high = m
    eps = 1e-6 # 1*10^-6
    while (high - low) > eps:
        mid = (low + high) / 2.0
        if multiply(mid, n) < m:
            low = mid
        else:
            high = mid
    if ceil(low)-low>0.001:
        return -1
    else:
        return ceil(low)