class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # num of subarrays of size k that avg >= threshold
        # pos must be preserved by definition
        # not guaranteed a sort

        if len(arr) < k:
            return 0

        num_subarrays = 0
        l = 0
        target_sum = threshold * k
        sum_of_window = None

        for l in range(len(arr) - k + 1): # normalize k to idx
            if sum_of_window is None:
                sum_of_window = sum(arr[:k])
            else:
                sum_of_window -= arr[l-1]
                sum_of_window += arr[l+k-1] # normalize k to idx

            if sum_of_window >= target_sum:
                num_subarrays += 1

        return num_subarrays
