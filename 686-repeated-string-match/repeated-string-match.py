class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        count = 0
        s = ""
        while len(s) < len(b):
            s = s + a
            count += 1
        if b in s:
            return count
        s = s + a
        count += 1
        if b in s:
            return count
        return -1

        