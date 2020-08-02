'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''

# Approach 1: Brute Force --> Time Limit Exceeded
# Time complexity: O(n^2), calculating n(n-1)/2 height pairs
# Space complexity: O(1), constant extra space is used

#def maxArea(self, height):
#    """
#    :type height: List[int]
#    :rtype: int
#    """
#    maxArea = 0
#
#    for i in range(len(height) - 1):
#        for j in range(i + 1, len(height)):
#            if height[i] < height[j]:
#                ht = height[i]
#            else:
#                ht = height[j]

#            w = j - i
#            area = ht * w

#            if area > maxArea:
#                maxArea = area

#    return maxArea

# Approach 2: Two pointers
# Moving the shorter line's pointer
# Time complexity: O(n), single pass
# Space complexity: O(1), constant space is used

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxArea = 0
    left = 0
    right = len(height) - 1

    while left < right:
        maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxArea

if __name__ == '__main__':
    solution = maxArea([1,8,6,2,5,4,8,3,7])
    # 49 (7 * 7)
    print(solution)