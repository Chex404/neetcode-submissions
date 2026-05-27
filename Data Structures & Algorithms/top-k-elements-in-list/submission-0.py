class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        freq = dict(sorted(freq.items(), key = lambda x: x[1], reverse = True))
        res = []

        for key, value in freq.items():
            if k == 0:
                break
            k = k - 1
            res.append(key)

        return res
        