class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace("-", "").upper()
        first_group = len(s) % k
        result = []
        if first_group != 0:
            result.append(s[:first_group])
        for i in range(first_group, len(s), k):
            result.append(s[i:i + k])
        
        return "-".join(result)
