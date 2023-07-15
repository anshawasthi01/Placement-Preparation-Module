# https://www.codingninjas.com/studio/problems/sort-a-stack_985275?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0
from os import *
from sys import *
from collections import *
from math import *

def sorted_insert(stack,p):

    if not stack or stack[-1]<p:

        stack.append(p)

        return

    s = stack.pop()

    sorted_insert(stack,p)

    stack.append(s)

 

def sortStack(stack):
    # given data structure is a python list 
    # as list have all the similar operations available so use them
    # Write your code here

    if not stack:

        return

    p = stack.pop()

    sortStack(stack)

    sorted_insert(stack,p)
