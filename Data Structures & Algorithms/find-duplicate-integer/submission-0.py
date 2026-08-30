class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        found = set()

        for i in range(len(nums)):
            if nums[i] not in found:
                found.add(nums[i])
            else:
                return(nums[i])

        