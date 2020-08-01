'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''
# Approach 1: Brute Force
# Time Complexity: O(mk)
# where k is the length of common prefix
# Space Complexity: O(k)

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    if len(strs) == 0:
        return ""

    answer = ""

    for i in range(len(strs[0])):
        for s in strs:
            if len(s) <= i or s[i] != strs[0][i]:
                return answer
        answer += strs[0][i]

    return answer

if __name__ == '__main__':
    solution = longestCommonPrefix(["flower","flow","flight"])
    # fl
    print(solution)
