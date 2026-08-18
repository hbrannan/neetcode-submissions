class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashed = defaultdict(int)
        for n in nums:
            if hashed[n]:
                return True
            else:
                hashed[n] += 1
        return False
        