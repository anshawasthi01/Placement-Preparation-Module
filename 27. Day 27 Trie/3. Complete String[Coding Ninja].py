# https://www.codingninjas.com/studio/problems/complete-string_2687860?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

from typing import *

'''

    Time Complexity : O(Sum(A[i])*max(A[i])*log(N))

    Space Complexity : O(Sum(A[i]))



    where 'Sum(A[i])' is the sum of size of all words 'A[i]',

    'max(A[i])' is the maximum size of string in array 'A'.

    and 'N' is the size of array 'A'.

'''



from typing import *



def completeString(n: int, a: List[str])-> str:



    ans = ""



    mp = {}


    # Storing all strings in hashmap.

    for i in range(n):

        mp[a[i]] = 1

    



    for i in range(n):

        pre = ""

        flag = True


        # Traversing over all prefixes of the string 'a[i]'.

        for j in range(len(a[i])):



            pre += a[i][j]

            # If current prefix is not present in map, this string is invalid.

            if pre not in mp:

                flag = False

                break

            

        # Current string is a valid string.

        if flag:

            # If current string is longer than ans, we update it.

            if len(ans) < len(a[i]):

                ans = a[i]

            # If current string is of same size as 'ans', but lexicographically smaller, we update it.

            elif len(ans) == len(a[i]) and a[i] < ans:

                ans = a[i]

            
        
    

    # If there is no valid answer, we return "None".

    if len(ans) == 0:

      ans = "None"

    
    # Return the final result.

    return ans