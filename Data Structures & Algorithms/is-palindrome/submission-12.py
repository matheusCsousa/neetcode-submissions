class Solution:
    def isPalindrome(self, s: str) -> bool:
        strN = ""

        for c in s:
            if c.isalnum():
                strN += c.lower()
        return strN == strN[::-1]
