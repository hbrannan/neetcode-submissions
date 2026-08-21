class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out = [0,0] # # numbers is ASC 1-indexed; i < j, i + j = target, i !=j

        # Use order, complement & compare to determine move of "pointers"
        i = 0
        j = -1

        # [1,2,3,4], target = 3
        for _ in range(len(numbers)): # Max num steps is full array
            start = numbers[i] # 3; 4 
            start_complement = target - start # -1

            end = numbers[j] # -4; 4
            end_complement = target - end # -1

            if end == start_complement: # No
                out[0] = i + 1
                out[1] = len(numbers) + j + 1
                break

            if start_complement > end: # 2 > 4 (leave)
                i += 1
            
            if end_complement < start: # -1 < 1 (adjust to next)
                j -= 1

        return out

