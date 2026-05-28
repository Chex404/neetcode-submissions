class Solution:
    def isPalindrome(self, s: str) -> bool:
        req_str = ""

        for ch in s:
            if ch.isalnum():
                req_str += ch.lower()

        if req_str == req_str[::-1]:
            return True
        else:
            return False
        