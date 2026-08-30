class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res