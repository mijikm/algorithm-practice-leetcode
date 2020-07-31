def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # Approach 1: Convert to string
    # Time Complexity: O(n)
    # where n == len(x)
    # Space Complexity: O(1)

    if (str(x) == str(x)[::-1]):
        return True
    else:
        return False

if __name__ == '__main__':
    solution = isPalindrome("-121")
    print(solution)
