class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for i in range(len(nums)):
            if nums[i] not in result:
                result.append(nums[i])
        for i in range(len(result)):
            nums[i] = result[i]
        return len(result)