class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
    # Approach 1: Brute Force
    # Time Complexity: O(n^3)
    # assume n is the length of the input string
    # verifying each substring takes O(n) time
    # Space Complexity: O(1)

    #    if len(s) <= 1 or s == s[::-1]:
    #        return s
    #    longest = ""

    #    for i in range(len(s)):
    #        for j in range(len(s), i, -1):
    #            if s[i:j] == s[i:j][::-1]:
    #                if len(s[i:j]) > len(longest):
    #                    longest = s[i:j]
    #    return longest

    # Approach 2: Expand around center
    # Time Complexity: O(n^2)
    # assume n is the length of the input string
    # as expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).
    # Space Complexity: O(1)
        if len(s) <= 1 or s == s[::-1]:
            return s
        longest = ""

        for i in range(len(s)):
            # odd case
            tmp = helper(s,i,i)
            if len(tmp) > len(longest):
                # update longest
                longest = tmp

            # even case
            tmp = helper(s,i,i+1)
            if len(tmp) > len(longest):
                longest = tmp

        return longest

def helper(s,l,r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1 # decrement the left
        r += 1 # increment the right

    return s[l+1:r]