# https://www.codingninjas.com/studio/problems/count-distinct-substrings_985292?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTab=0

'''
    Time Complexity: O(N^3)
    Space Complexity: O(N^2)

    Where 'N' is the length of the given string.
'''


def countDistinctSubstrings(s):
    # Set to store all our substrings
    store = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Inserting the current substring
            store.add(s[i:j + 1])

    # Return the length of the set + 1 for empty substring
    return len(store) + 1