class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0 
        count = 0 # initializes at 1 for el.0

        for r in range(0, len(nums)):
            # First, take count.
            if nums[r] == nums[r - 1]:
                count += 1

                if count <= 2: 
                    nums[l] = nums[r]
                    l += 1
            else: # ne
                count = 1
                nums[l] = nums[r]
                l += 1


        # nums = nums[:min(l, len(nums))]
        return l
    



'''
This could be sliding window problem: L & R will move at different speeds. There are brute force solves (n^3) and memory solves (hash_map: occurrences) that we can then print up to 2 but we should be able to do this in linear time and constant memory.
'''
        