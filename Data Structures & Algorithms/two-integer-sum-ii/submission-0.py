class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        for i in range(len(numbers)):
            req = target - numbers[i]
            if req in numbers and i != numbers.index(req):
                return [i+1, numbers.index(req)+1]
