class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            stones.sort()
            r1 = stones.pop()
            r2 = stones.pop()   
            if r1 != r2:
                stones.append(r1 - r2)
        if len(stones) == 0:
            return 0
        return stones[0]

        