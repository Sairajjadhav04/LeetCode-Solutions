class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        t = 0
        target = tickets[k]
        for i, ti in enumerate(tickets):
            if i <= k:
                t += min(ti, target)
            else:
                t += min(ti, target - 1)
        return t    