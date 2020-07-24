class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_table = {}
        my_list = []
        sub_length = 0

        for i in range(len(s)):
            if s[i] not in my_list:
                my_list.append(s[i])
                sub_length = len(my_list)
            else:
                hash_table[str(my_list)] = sub_length
                my_list = []
                sub_length = 0
                my_list.append(s[i])
                sub_length = len(my_list)

        if hash_table is not None:
            return max(hash_table.values())
        else:
            return sub_length
