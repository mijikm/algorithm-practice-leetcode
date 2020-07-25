class Solution(object):
    # 1. Approach: Count only indexes
    # - Find last occurrence of the char, and calculate length of the string
    #   between current pointer and last occurrence of the char + 1

    # Time Complexity: O(n)
    # assume that n represents the length of the string "s"

    # Space Complexity: O(1)
    # since it is limited to only 26+ chars

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left_valid_letter = 0
        longest = 0
        last_seen = {}

        for i, letter in enumerate(s):
            if letter in last_seen:
                # left_valid_letter must be greater than any position which is seen again
                # left_valid_letter is 1 index greater than the last seen letter's index
                left_valid_letter = max(left_valid_letter, last_seen[letter] + 1)

            # update the dictionary with the letter and the index
            last_seen[letter] = i

            # Length of substring from left_valid to i is "i - left_most_valid + 1"
            longest = max(longest, i - left_valid_letter + 1)

        return longest




