class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print('NUMS', nums)
        # 9,4,7,3,5,8,6
        # -1,0,1
        # 3,4,5,6,7,6,9
        # 
        longest = []
        # Cannot sort bc linear time
        # They won't be ordered so you may need to look before or after
        # Maybe something close to bucket sort where you store in arr leaving gaps but O(highest #)

        # min heap is O(n)
        # Then pop thru heap comparing
        length = len(nums)
        if not length: 
            return 0

        heapq.heapify(nums)

        highest_count = 1
        current_count = 1
        current_num = heapq.heappop(nums)

        for i in range(length-1):
            next_num = heapq.heappop(nums)

            if next_num == current_num:
                continue

            is_continuing_sequence = next_num - current_num == 1
            if is_continuing_sequence:
                # while consecutive, increment current count
                current_count +=1
            # If it is not, compare and possibly update highest count
            if current_count > highest_count:
                highest_count = current_count

            if not is_continuing_sequence: 
                current_count = 1

            current_num = next_num
        
        return highest_count

        # What if there are 2 consec seq of equal length?
        