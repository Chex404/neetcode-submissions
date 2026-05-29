class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_index = {}
        start = 0
        max_len = 0

        for i, ch in enumerate(s):
            if ch in start_index and start_index[ch] >= start:
                start = start_index[ch] + 1
            start_index[ch] = i
            max_len = max(max_len, i - start + 1)
        return max_len
        