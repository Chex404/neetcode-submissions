class Solution:
    def isPalindrome(self, s: str) -> bool:
        c_s = ""
        for ch in s:
            if ch.isalnum():
                c_s += ch.lower()

        return c_s == c_s[::-1]
        