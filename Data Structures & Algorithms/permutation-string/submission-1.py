class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_s1 = {}
        freq_curr = {}

        for ch in s1:
            freq_s1[ch] = 1 + freq_s1.get(ch, 0)

        # Build first window
        for i in range(len(s1)):
            freq_curr[s2[i]] = 1 + freq_curr.get(s2[i], 0)

        if freq_curr == freq_s1:
            return True

        l = -1
        # Slide the window
        for r in range(len(s1), len(s2)):
            # Add new right char
            freq_curr[s2[r]] = 1 + freq_curr.get(s2[r], 0)

            # Remove old left char
            l += 1
            freq_curr[s2[l]] -= 1
            if freq_curr[s2[l]] == 0:
                del freq_curr[s2[l]]

            if freq_curr == freq_s1:
                return True

        return False