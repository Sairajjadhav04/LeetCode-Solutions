class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = sum(nums[::2])
        odd = sum(nums[1::2])
        left_even = 0
        left_odd = 0
        count = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                even -= nums[i]
            else:
                odd -= nums[i]
            new_even = left_even + odd
            new_odd = left_odd + even
            if new_even == new_odd:
                count += 1
            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]
        return count