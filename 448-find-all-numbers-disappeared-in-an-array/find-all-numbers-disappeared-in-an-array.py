class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [] 
        n = len(nums)
        new = set(nums)
        for i in range(1,n+1):
            if i not in new :
                res.append(i)
        return res
        