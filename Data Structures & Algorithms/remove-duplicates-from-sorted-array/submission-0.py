class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # O(n) memory; hash, output in (On) time
        # .remove() uses O(n2) but 2 Pointer can reduce to O(n)

        if not nums:
            return nums

        prev = nums[0] 
        is_rearranging = False
        l, r = 0, 1
        unique_chars = 1 # exclusion-based for upcoming slice

        # nums=[1,1,2,3,4]
        while r < len(nums): 
            num = nums[r]
            
            if is_rearranging: 
                if num > prev:
                    nums[l] = num
                    l += 1
                    unique_chars += 1
            elif num == prev:
                l = r 
                is_rearranging = True 
            else:
                is_rearranging = False
                unique_chars += 1

            if num > prev:
                prev = num # Must happen after comparisons

            r += 1

        nums = nums[:unique_chars]

        return len(nums)
        