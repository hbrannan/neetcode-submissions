class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            for j, num_again in enumerate(nums):
                if i == j:
                    continue
                if num + num_again == target:
                    return [min(i, j), max(i, j)]
        