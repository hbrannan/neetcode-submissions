class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Note: both position and value matter
        # Does > 2 matter? Does which index is assigned to which matter?
        l, r = 0, 1
        length = len(nums)
        # nums=[1,2,2,3]

        while l <= length - 2:
            left_val = nums[l]
            right_val = nums[r]

            # print(left_val, right_val)
            # print(abs(r-l), k, abs(r-l) <= k)
            
            # First, perform check.
            if abs(r-l) <= k and left_val == right_val:
                return True
            
            # Next, define next step.
            if r == length - 1 or abs(r-l) > k:
                l += 1
                r = l + 1
            else:
                r += 1

        # R continues to move until R-L <= k
        # this must include to the last index

        # if R hits last idx OR R-L > k then
        # L needs to shift 1 and R needs to be 1 more than L

        # as long as r-l > k
        # if left el === right el return true

        # L should get to 2nd of last idx then useless to keep moving it
            

        return False
        


        # while r < len(nums) and l < r:
        #     left = nums[l]
        #     right = nums[r]
        #     print(f'{l},{r}', f'ELS {left},{right}')

        #     print(abs(r-l), '<=', k)
        #     if abs(r-l) <= k:
        #         if left == right:
        #             return True
        #         r += 1
        #     else:
        #         l += 1
        #         r = l + 1