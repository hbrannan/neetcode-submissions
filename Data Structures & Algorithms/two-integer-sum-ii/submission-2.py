class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out = [0,0] # numbers is ASC 1-indexed; i < j, i + j = target, i !=j

        # Use order, complement & compare to determine move of "pointers"
        i = 0
        j = -1

        for _ in range(len(numbers)): # Max num steps is full array
            start = numbers[i] 
            start_complement = target - start 

            end = numbers[j] 
            end_complement = target - end 

            if end == start_complement: 
                out[0] = i + 1
                out[1] = len(numbers) + j + 1
                break

            if start_complement > end: 
                i += 1
            
            if end_complement < start: 
                j -= 1

        return out

