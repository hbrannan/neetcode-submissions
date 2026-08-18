import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_frequencies = defaultdict(int)
        # {1: 1, 2:2, 3:3}
        for num in nums:
            val_frequencies[num] += 1
        
        all_frequencies = []
        # [(3,3) (2,2), (1,1)]
        for num in val_frequencies.keys():
            heapq.heappush_max(all_frequencies, (val_frequencies[num], num))
        highest_k_occurrences = []        
        for count in range(k):
            max_frequencey_pair = heapq.heappop_max(all_frequencies)
            highest_k_occurrences.append(max_frequencey_pair[1])
        
        return highest_k_occurrences

        