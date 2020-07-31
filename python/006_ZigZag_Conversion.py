def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    # Approach 1: Iterate and Assign the character to the row
    # Time Complexity: O(n)
    # where n == len(s)
    # Space Complexity: O(n)

    if numRows == 1:
        return s

    # initialise result with empty string
    result = [""] * numRows
    # row number starts from 0 /first row
    row = 0
    # move down is 1, move up is -1
    direction = 1

    for i in range(len(s)):
        result[row] += s[i]
        # when moving down and not the last row
        if row < numRows - 1 and direction == 1:
            row += 1
        # when moving up and not the first row (row 0)
        elif row > 0 and direction == -1:
            row -= 1
        # when reaching the first (row 0) or the last row
        else:
            direction *= -1
            row += direction

    return ''.join(result)

if __name__ == '__main__':
    solution = convert("PAYPALISHIRING",3)
    print(solution)