class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        # if len(nums) == 1:
        #     return nums[0]

        max_sum = nums[0]
        st, i = 0, 0
        current_sum = 0

        while i < len(nums): 
            if current_sum < 0:
                current_sum = 0
                st = i

            current_sum += nums[i]
            max_sum = max(current_sum, max_sum)

            i += 1

        return max_sum
        