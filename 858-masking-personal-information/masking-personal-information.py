class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        if "@" in s:
            s = s.lower()
            name, domain = s.split("@")
            return name[0] + "*****" + name[-1] + "@" + domain

        else:
            digits = ""
            for ch in s:
                if ch.isdigit():
                    digits += ch
            country_code_length = len(digits) - 10
            last_four = digits[-4:]
            if country_code_length == 0:
                return "***-***-" + last_four
            return "+" + "*" * country_code_length + "-***-***-" + last_four
