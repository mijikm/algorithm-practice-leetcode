def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    # Approach 1: Check negative and validate
    # Time Complexity: O(n)
    # where n == len(x)
    # Space Complexity: O(1)

    # set default neg value to False
    neg = False
    # if negative value
    if x < 0:
        neg = True
        # convert to positive value
        x = x * -1
    # reverse string
    s = str(x)[::-1]
    # convert to integer
    n = int(s)

    # negative value
    if neg == True and abs(n) < 2 ** 31 - 1:
        # convert to original negative value
        return n * -1
    # positive value
    elif abs(n) < 2 ** 31 - 1:
        return n
    # not 32-bit signed integer range
    else:
        return 0

if __name__ == '__main__':
    solution = reverse(-2148)
    print(solution)