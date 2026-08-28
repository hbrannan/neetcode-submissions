class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # what is a monotonic queue? / relative position must be preserved w/ value
        if not nums: 
            return 0
        stop = len(nums)
        max_sum = nums[0]

        current_sum = nums[0] 
        l, r, = 0, 1
        current_window_len = 2 

        while l <= stop: # circle back to idx0 for full loop

            if current_window_len > stop: 
                # Slide the L to the R (variable size desired); cte
                l += 1
                r = l + 1
                current_sum = nums[l % stop] 
                current_window_len = 2 # r - l + 1 (count-based)
                
            if current_sum < 0:
                l = r
                r += 1
                current_sum = nums[l % stop] 
                current_window_len = 2
            else:
                current_window_len += 1
                current_sum = current_sum + nums[r % stop]      
                r += 1

            max_sum = max(current_sum, max_sum)
        
        return max_sum

        