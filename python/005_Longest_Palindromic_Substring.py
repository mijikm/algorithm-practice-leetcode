class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1 or s == s[::-1]:
            return s

        start = 0
        max_length = 1

        for i in range(len(s)):
            odd = s[i - max_length - 1: i + 1]
            even = s[i - max_length: i + 1]
            if i - max_length - 1 >= 0 and odd == odd[::-1]:
                start = i - max_length - 1
                max_length += 2
            elif i - max_length >= 0 and even == even[::-1]:
                start = i - max_length
                max_length += 1

        return s[start: start + max_length]
