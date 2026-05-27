class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}

        for ch in s:
            if ch not in hash_map:
                hash_map[ch] = 1
            else:
                hash_map[ch] += 1

        for ch in t:
            if ch not in hash_map or hash_map[ch] == 0:
                return False

            elif hash_map[ch] > 0:
                hash_map[ch] -= 1

        return True
         