class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # need to get the equation for volume (lxwxh?); triangles?
        # w = diff of indices
        # nope this is actually a 2d space but w/ 2 diff heights; minimum height wins
        # w * min of heights
        # O(n) time; O(1) space

        # height=[1,7,2,5,4,7,3,6]

        max_area = 0 # 7
        l = 0
        r = len(heights) - 1

        while r > l: # 0, 8
            l_val = heights[l] # 1
            r_val = heights[r] # 7
            min_h = min(l_val, r_val) # 1
            width = r - l # 7 - 0 -> 7
            area = width * min_h # 7 * 1 = 7

            if area > max_area:
                max_area = area
            
            if l_val <= r_val:
                l += 1
            else:
                r -= 1

        return max_area 

        # Brute force is not needed because we can fully eliminate a choice at each step
        # This is because you're using the min height only to calculate area so the width is already maxed
        # width = len(heights)

        # while width:
        #     r_idx = length - 1
        #     l_idx = length - width

        #     while r_idx > l_idx
        #         min_of_heights = min(heights[r_idx], heights[l_idx])
        #         v = min_of_heights * width
        #         if v > max_volume: 
        #             max_volume = volume
                
        #         width -= 1
