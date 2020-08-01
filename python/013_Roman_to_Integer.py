'''
Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
'''
# Approach 1: Traverse considering six instances
# Time Complexity: O(n)
# where n == len(s), only one traversal of the string is required.
# Space Complexity: O(1)
# no extra space is required.

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    # create a dictionary with roman numerals
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    answer = 0

    for i in range(len(s)):
        # find six instances where subtraction is used
        if i > 0 and roman[s[i]] > roman[s[i - 1]]:
            # need to subtract 2*roman[s[i-1]] as it was already added
            answer += roman[s[i]] - 2 * roman[s[i - 1]]
        else:
            answer += roman[s[i]]

    return answer

if __name__ == '__main__':
    solution = romanToInt("MCMXCIV")
    # 1994, M = 1000, CM = 900, XC = 90 and IV = 4
    print(solution)
