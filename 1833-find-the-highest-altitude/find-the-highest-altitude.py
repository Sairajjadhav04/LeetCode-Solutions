class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0
        high = 0 
        for i in gain :
            altitude += i 
            high = max(high,altitude)
        return high