class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []

        for i in range(len(nums)):
            req = target - nums[i]

            if req in nums and nums.index(req) != i:
                
                output.append(min(i, nums.index(req)))
                output.append(max(i, nums.index(req)))
                return output