class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # can be negative numbers; contiguous
        min_len = None
        l = 0
        running_sum = 0

        # building running sum through all steps:
        # at each step, decide to expand right or shrink left
        # final element will be absolute last one
        # right will move by 1 each time, bu we need to be able to "pause and loop" on left at any time
        # we will start r @ l = 0, and so only need to track 1 "num" var

        # since you want the minimum, you're going to need an initiator comparison for min_len

        # stop when: at end or >= target
        # -- first calc and check minLen
        # -- then reset L; R can  (and so running_sum)
        # [2,1,5,1,5,3]

        for r, num in enumerate(nums):
            running_sum += num
            while running_sum >= target and l < len(nums):
                # update min
                this_len = r - l + 1
                min_len = this_len if min_len is None else min(min_len, this_len)
                # next
                running_sum -= nums[l]
                l += 1

        return min_len or 0
        