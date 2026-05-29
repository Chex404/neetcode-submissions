class Solution:
    def maxArea(self, heights: List[int]) -> int:

        

        max_area = 0

        for l in range(len(heights)):
            r =  len(heights) - 1
            while l < r:
                h = min(heights[l], heights[r])
                w = r - l  
                area = h * w

                if area > max_area:
                    max_area = area

                r = r-1

        return max_area

            
        