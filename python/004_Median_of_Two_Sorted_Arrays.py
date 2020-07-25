class Solution(object):
    # 1. Approach: Brute Force / Sort and find
    # - Put two arrays together and find median

    # Time Complexity: O(m+n)
    # due to sorting time
    # Space Complexity: O(m+n)

    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """

    #     nums1.extend(nums2)
    #     nums1.sort()

    #     if len(nums1) % 2 == 0:
    #         i = len(nums1) // 2
    #         ans = float(nums1[i] + nums1[i - 1]) / 2
    #         return ans
    #     else:
    #        i = len(nums1) // 2
    #         ans = float(nums1[i])
    #        return ans


    # 2. Approach: Binary Search
    # - partition both arrays into equal halves
    # e.g. x1 x2 | x3, x4, x5
    #      y1 y2 y3 y4 | y5 y6 y7
    # - then check if x2 <= y5 and y4 <= x3
    # - median is avg(max(x2,y4), min(x3,y5)
    # - if combined elements is odd (one more element on the left side), avg(max(x2,y4))

    # Time Complexity: O(log(min(m,n)))
    # m and n are the length of two arrays respectively

    # Space Complexity: O(1)
    # only need constant memory to store local variables

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # ensure first part is smaller than second
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)

        low = 0
        high = x

        while low <= high:
            partitionX = (low + high) // 2
            # partition the second array
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = nums1[partitionX - 1] if partitionX > 0 else float('-inf')
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = nums2[partitionY - 1] if partitionY > 0 else float('-inf')
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # check the partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return (max(maxLeftX, maxLeftY))

            # if not, move partitioning
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1