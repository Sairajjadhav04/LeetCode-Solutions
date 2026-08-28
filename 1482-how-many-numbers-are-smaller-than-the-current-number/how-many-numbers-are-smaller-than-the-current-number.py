class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res =[] 
        for i in range(0,len(nums)):
            count = 0
            for j in range(0,len(nums)):
                if (j != i and nums[i]>nums[j]):
                    count = count+1
            res.append(count)
        return res
                
                