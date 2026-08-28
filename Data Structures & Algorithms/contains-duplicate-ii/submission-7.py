class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Note: both position and value matter
        # Does > 2 matter? Does which index is assigned to which matter?
        l, r = 0, 1
        length = len(nums)

        while l <= length - 2:
            left_val = nums[l]
            right_val = nums[r]
            
            # First, perform check.
            if abs(r-l) <= k and left_val == right_val:
                return True
            
            # Next, define next step.
            if r == length - 1 or abs(r-l) > k:
                l += 1
                r = l + 1
            else:
                r += 1
        return False
        