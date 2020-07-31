def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    # Approach 1: Validate
    # Time Complexity: O(n)
    # where n == len(str)
    # Space Complexity: O(1)

    # remove white spaces
    s = str.strip()
    # check if it is empty or starts with letter or .
    if len(s) == 0 or s[0].isalpha() or s[0] == ".":
        return 0
    # check - or + sign
    neg = False
    if s[0] == "-":
        neg = True
        s = s[1:]
    elif s[0] == "+":
        s = s[1:]

    answer = ""

    for i in range(len(s)):
        # s[0] is always digit
        if s[i].isdigit() == False:
            break
        elif s[i].isdigit() == True:
            answer += ''.join(s[i])

    # if answer is empty e.g. s == "-"
    if answer.isdigit() == False:
        return 0

    # convert to integer
    n = int(answer)
    # negative
    if neg == True and n <= 2 ** 31 - 1:
        n = n * -1
        return n
    # positive
    elif n <= 2 ** 31 - 1:
        return n
    # negative and out of range
    elif neg == True:
        return -2 ** 31
    # positive and out of range
    else:
        return 2 ** 31 - 1

if __name__ == '__main__':
    # try -, +, .1, 3.15, -57
    solution = myAtoi("-")
    print(solution)
