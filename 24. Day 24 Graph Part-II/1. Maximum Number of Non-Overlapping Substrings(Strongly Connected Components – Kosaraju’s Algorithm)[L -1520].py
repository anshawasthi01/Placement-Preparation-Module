# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/description/

class Solution:
    def maxNumOfSubstrings(self, s: str):
        """
        Given a string s of small case letters, this program
        determines the maximum number of substrings of minimum
        size and returns the resulting list of substrings to
        the caller.

        :param s: string of small case letters
        :type s: str
        :return: list of non-overlapping substrings
        :rtype: list[str]
        """
        set_s = set( s )

        """
        Create dictionary (letter_ranges) to store the minimum and
        maximum indexes for each letter within s. For each letter,
        the letter range is the [minimum, maximum] index pair.
        """
        letter_ranges = {}
        for k, letter in enumerate( s ):
            if letter in letter_ranges:
                letter_ranges[letter][1] = k
            else:
                letter_ranges[letter] = [k, k]

        """
        For each letter range, determine the set of letters within
        the range. Store the set for each letter in letter_sets.
        """
        letter_sets = {}
        for letter in letter_ranges:
            left, right = letter_ranges[letter]
            letter_sets[letter] = set( s[left:right + 1] )

        """
        Expand each letter set to include, by Union operator,
        the letter set for each letter within the set.
        - letter_key identifies the letter whose letter set is
          being expanded.
        - The set visited is used to prevent duplicate inclusion
          of a letter set into the expanded letter set.
        """
        for letter_key in letter_sets:
            queue = []
            visited = set()
            for letter in letter_sets[letter_key]:
                queue.append( letter )
                visited.add( letter )
            letter_set = set()
            while queue:
                letter = queue.pop( 0 )
                letter_set = letter_set.union( letter_sets[letter] )
                for qletter in letter_sets[letter]:
                    if not qletter in visited:
                        queue.append( qletter )
                        visited.add( qletter )
            letter_sets[letter_key] = letter_set

        """
        From the expanded letter sets and letter ranges, create
        the intervals from which the substrings will be derived.
        """
        intervals = []
        for letter_key in letter_sets:
            letter_set = letter_sets[letter_key]
            left = len( s )
            right = -1
            for letter in letter_set:
                new_left, new_right = letter_ranges[letter]
                left = min( left, new_left )
                right = max( right, new_right )
            if not [left, right] in intervals:
                intervals.append( [left, right] )

        """
        Remove the intervals that contain other intervals.
        The surviving intervals will be non-overlapping.
        """
        intervals.sort()
        k = 0
        while k < len( intervals ) - 1:
            if intervals[k][1] > intervals[k + 1][1]:
                intervals.pop( k )
            else:
                k += 1

        """
        Use the non-overlapping intervals to create the list of
        substrings that is returned from this program.
        """
        substrings = []
        for left, right in intervals:
            substrings.append(s[left:right + 1])
        return substrings