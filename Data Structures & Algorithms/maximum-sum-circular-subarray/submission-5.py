class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # what is a monotonic queue? / relative position must be preserved w/ value
        if not nums: 
            return 0

        # nums=[1,2,3,4,5]

        stop = len(nums)
        max_sum = nums[0]

        current_sum = nums[0] # IN PROCESS: shifting this & r
        l, r, = 0, 1
        current_window_len = 2 

        print('length', stop)

        while l <= stop: # circle back to idx0 for full loop
            print(f'{nums[l%stop]},{nums[r%stop]} w/', current_sum)

            if current_window_len > stop: 
                print('SHIFTING')
                # print(f'SLIDE {l},{r} of {current_window} len')
                # Slide the L to the R (variable size desired); cte
                l += 1
                r = l + 1
                current_sum = nums[l % stop] 
                current_window_len = 2 # r - l + 1 (count-based)
                print('>> current_sum', current_sum)
                
            if current_sum < 0: # and isn't the same as L
                l = r
                r += 1
                current_sum = nums[l % stop] 
                current_window_len = 2
            else:
                # Process value at *this r*
                current_window_len += 1
                current_sum = current_sum + nums[r % stop]      
                r += 1

            max_sum = max(current_sum, max_sum)
        
        return max_sum

        