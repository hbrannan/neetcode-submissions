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


'''
Critique of solve post-solution video: 

1. Should lean further into the idea that the solution is in the "already seen / processed" array to deal with less code + chars:
- r should start processing @ 1 because 0 by definition must be unique
- l, if it starts at 1 will equate to the unique chars count 
- prev, can just be r - 1
-- By doing this, you simplify set up.

2. To collapse / simplify the == and the > than checks into 1, you can use the set ups assumption that it is ALWAYS not smaller, so if it is not equal, then proceed.

SIMPLER SOLVE 

l = 1

for r, el in range(1: len(nums)):
    if el != nums[r-1]:
        nums[l] = el
        l += 1
return l


ALT SIMPLE SOLVE

    n = len(nums)
    l = r = 0
    while r < n:
        nums[l] = nums[r]
        while r < n and nums[r] == nums[l]:
            r += 1
        l += 1
    return l

* One slows the advance of l while condition is not met; the other zooms advance of r until condition is met *

Other learnings: 
- A sorted set maintains order

Other questions: 
- Why is conversion to a sorted set O(nlogn) and a min heap O(n)?
--- I think it has something to do with the "bucket sort" method and that fact you can only get the min, can't iterate thru idxes of min heap in sorted order

'''
