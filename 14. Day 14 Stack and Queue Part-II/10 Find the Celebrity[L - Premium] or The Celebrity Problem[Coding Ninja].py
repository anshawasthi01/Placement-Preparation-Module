# https://leetcode.com/problems/find-the-celebrity/
# https://www.codingninjas.com/studio/problems/the-celebrity-problem_982769?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''
    This is signature of helper function 'knows'.
    You should not implement it, or speculate about its implementation.

    def knows(int A, int B); 
    Function 'knows(A, B)' will returns "true" if the person having
    id 'A' knows the person having id 'B' in the party, "false" otherwise.
'''

def findCelebrity(n, knows):
    st = []    
    for i in range(n):
        st.append(i)
    
    while len(st) > 1:
        b = st.pop() # assume celeb
        while st and knows(st[-1], b):
            a = st.pop()
        if not st:
            st.append(b)
            
    for i in range(n):
        if i != st[-1] and (not knows(i, st[-1]) or knows(st[-1], i)):
            st.pop()
            break
    
    return -1 if not st else st[-1]
