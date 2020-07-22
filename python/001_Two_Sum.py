class Solution(object):

    # 1. Brute Force / Naive Solution
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    #
    # def twoSum(self, nums, target):
    #    """
    #    :type nums: List[int]
    #    :type target: int
    #    :rtype: List[int]
    #    """
    #    my_list = []
    #
    #    for i in range(len(nums)):
    #        for j in range(i + 1, len(nums)):
    #            if (nums[i] + nums[j] == target):
    #                my_list.extend([i, j])
    #                return my_list

    # 2. Hash Table
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # - The extra space required depends on the number of items stored

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table:
                # return sorted([i, hash_table[complement]])
                return [i, hash_table[complement]]
            hash_table[nums[i]] = i
